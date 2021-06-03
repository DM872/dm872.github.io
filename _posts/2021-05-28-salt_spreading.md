---
layout: default
mathjax: true
title:  Assignment 2
date:   2021-05-28 00:33:19 +0100
categories: assignments 
---

**Deadline: Monday, June 28, 2021, at 11:59 am.**

For questions on the assignment, use the [Discussion Board under
Resources in LMS](https://sdu.itslearning.com/ContentArea/ContentArea.aspx?LocationID=9315&LocationType=1).

## Assignment 2

This is the second assignment. It will be graded and will contribute to your final
assessment in the course.

The assignment has to be carried out individually.

To complete the assignment you have to submit in [LMS] a `.tgz` or
`.zip` archive containing:

- a report in pdf format as concise as possible (by no way more than 10 pages) with the answers to the tasks

- the Python code for the calculations.

A [template]({{ "/assets/template_answers.tex" | absolute_url }}) for the report.




### Problem Description



In the winter season, roads need to be salted within a short period of
time when forecasts announce temperatures below the freezing
point.  The *salt spreading problem* consists in planning the sequence
of roads to salt while minimizing the total traveled distance. It can
be modelled as a generalization of the *capacitated arc routing problem*
[3] where road segments to be salted are represented as arcs to be
visited.

The goal of this project is to study an exact mathematical programming
approach for finding an optimal set of routes for salt spreading in
the municipality of Kerteminde.

More precisely the *salt spreading problem* that you have to address
is the following. You are given a fleet of vehicles and a network with
some arcs that require to be salted and other arcs that can be
traversed. The fleet of vehicles consists of two vehicles that depart
from their respective home nodes. The load of salt that the vehicles
can carry is in general insufficient to cover all arcs that require
salt therefore routes might include reloading at opportune
depots. After having salted the required arcs, the vehicles visit a
depot where they are reloaded with salt before heading home, ready for
the next day.  <!-- There is a maximum time of 210 minutes (3 hours
and a half) for completing the task. --> It is assumed that the
vehicles are "off duty" after the final reload, hence the path from
the depot to home does not count in the cost calculation.  The task is
to find a set of routes for the two vehicles such that each vehicle:

- uses only arcs available in the given network 

- traverses all required arcs depositing the needed amount of salt

- has always enough load of salt, that is, the load after serving a
  required arc cannot become negative (capacity constraints)

- the required arcs are salted within 210 minutes (3 hours and a half) 

- does not perform an U-turn at some selected nodes where they can be avoided

and the total distance travelled by the two vehicles is minimized. The
vehicles have to visit a depot before returning home, therefore they
start with a full cargo of salt and fuel. The path from the depot
to home does not count in the traveling time and distance.





### Data and code 

In the course repository [GIT] you find the input data and some
starting python code to: read the data, report some statistics and
plot the network. The data are real life data but unfortunately
the geographical coordinates are missing, hence plotting is done with
graph drawing algorithms for the placement of the points that may be
misleading.


![instance]({{ "/assets/images/data_excerpt.png" | absolute_url }}){:width="70%" .center-image }


Each row describes a node ("Knude punkt") and the set of edges
containing that node. The column "status" indicates whether an
edge needs to be salted and in which direction. A status of 1
indicates that the edges need to be salted but the direction is
free. A status of 2 indicates that the edge must be salted in a
predefined direction. A status of 3 indicates that the edge does not
need to be salted. We assume that all edges listed can be traversed in
both directions when salt is not deposited.
In addition, each edge has a column indicating the length of the road ("laengde") 
and a column indicating the breadth of the road ("salt m"), both
represented in meters. 

The vehicles are identical. They have a salt
capacity of $12.3 \mathrm{m}^3$ and they spread $30\textrm{ml}$ of salt
per $\mathrm{m}^2$ of road. Since, $1\textrm{ml} = 1
\mathrm{cm}^3=10^{-6}\mathrm{m^3}$, on each road segment of length $\ell$
and width $w$ (expressed in $\mathrm{m}$), they use $30\cdot 10^{-6} \cdot
\ell \cdot w\mathrm{m}^3$ of salt. 
Since roads are both urban and in the country side
we can assume an average speed of $65 \mathrm{Km/h}$.


The depots are in node 1 and in node 179 and the two drivers start and
end at their homes at node 2 and 130, respectively.


The data reader in python organizes the network data as a mixed graph
with further information on the links. A *mixed graph* is a graph made
of both edges and arcs. Edges can be traversed in either of the two
directions while arcs can only be traversed in their direction.  In
particular, the mixed graph provided by the reader is $G=(V,A \cup
A_{R} \cup E_{R})$. The set of nodes $V$ includes the set of road
intersections $I$, the set of refilling depots $D$ and the set of
homes $H$, that is, $V=I \cup D \cup H$. Each vehicle has a single
location $h$ from $H$ from which it departs and returns.  The set of
arcs $A$ contains the arcs that can be traversed while $A_R$ and $E_R$
arcs and edges, respectively, that are required to be
traversed. (Hence, edges that can be traversed in either direction
have been rewritten in $A$ as two antiparallel arcs.) Edge is $E_R$
are labeled $ij$ with $i<j$. There are no self loops.

<!-- This graph is obtained 
by substituting
every edge $(i,j) \in E$ by two antiparallel arcs $(i,j)$ and $(j,i)$
and keeping the required arcs, thus getting the sets ${A} =
\hat{A}\cup\{(i,j),(j,i) : (i,j) \in E\}$ and $R = A_R\cup\{(i,j),(j,i): (i,j)
\in E_R\} \subseteq \hat{A}$.
 
Let
$\hat{G}=(V,\hat{A}\cup E)$ be the mixed graph representing the road
network. The set of arcs $\hat{A}$
represents all traversable arcs and it includes the set $A_R$ of arcs
required to be salted. The set $E$ represents the set of edges that
can be traversed in both directions and it includes the set $E_R$ of
edges that are required to be salted.

 transforms $\hat{G}$ in a graph $G=(V,A \cup A_{R} \cup E_{R})$ by substituting
every edge $(i,j) \in E$ by two antiparallel arcs $(i,j)$ and $(j,i)$
and keeping the required arcs, thus getting the sets ${A} =
\hat{A}\cup\{(i,j),(j,i) : (i,j) \in E\}$ and $R = A_R\cup\{(i,j),(j,i): (i,j)
\in E_R\} \subseteq \hat{A}$.
 
-->

Beside the Kerteminde instance a few small instances are also made
available in the python scripts that can be useful for testing. The
most complete small instance can be loaded with the function
`load_example_Gualandi`. The instance is also depicted here:

![instance]({{ "/assets/images/gualandi.jpg" | absolute_url }}){:width="50%" .center-image }

Links from $E_R$ have been emphasized in red and those from $A_R$ in grey.
The corresponding data that can be used in python are:

```python
vehicles = {1: {'home': 0, 'capacity': 50.0}}
depots = {7: {'refill': 50.0}}
A = {(0, 1): {'len': 6}, (2, 4): {'len': 5}, (1, 2): {'len': 8}, (3, 4): {'len': 8}, (5, 7): {'len': 10}, (2, 3): {'len': 10}, (5, 6): {'len': 5}, (2, 5): {'len': 7}, (1, 3): {'len': 5}, (4, 7): {'len': 8}, (1, 0): {'len': 6}, (4, 2): {'len': 5}, (2, 1): {'len': 8}, (4, 3): {'len': 8}, (7, 5): {'len': 10}, (3, 2): {'len': 10}, (6, 5): {'len': 5}, (5, 2): {'len': 7}, (3, 1): {'len': 5}, (7, 4): {'len': 8}}
A_R = {(3, 4): {'dem': 20}, (6, 5): {'dem': 30}}
E_R = {(1, 2): {'dem': 30}}
```

Note that while this instance has nodes labelled from $0$ the
Kerteminde instance uses labels from $1$.


You can reproduce the example with the code provided by:

```python
python3 main.py
```

while for reading the Kerteminde instance you must use:
```python
python3 main.py -f ../data/kerteminde.csv
```

### Remarks

You are encouraged to maintain the notation for the network provided
above and to use the following terms with the meaning defined.

A *trip* is a sequence of arcs and edges visited by a vehicle that
departs from home or from a depot and arrives at home or at a depot. A
*route* is a sequence of trips performed by a vehicle that departs
from home and arrives at home.

Also, denote by $K$ indexed by $k$ the set of vehicles and by $T$
indexed by $t$ the set of all trips. Thus $T^k \subseteq T$ is the set
of trips making the route of the vehicle $k \in K$.


In case of need, the python code contains also the *pairing algorithm*
  to retrieve the routes from the selection of the arcs (see [1]). The
  function `derive_route` takes in input a dictionary with the vehicle
  identifiers as keys and an array of selected arcs for each
  corresponding vehicle as values and prints the routes.

The set of nodes $U\subseteq V$ at which U-turns cannot be avoided is
characterized as follows. Let:
- $a^+(\{u\})$ be the set of nodes that we can reach by an arc in $A \cup A_R$ leaving $u$ 
- $a^-(\{u\})$ be the set of nodes from which we can reach $u$ by an arc in $A \cup A_R$ 
- $a(\{u\})$ be the set of nodes linked to $u$ by an edge in $E_R$ 

Then the set $U \subseteq V$ contains all nodes $u\in V$ that satisfy one of the following conditions:

- $\|a(\{u\})\|=1$ and $\|a^+(\{u\})\|=\|a^-(\{u\})\|=0$
- $\|a(\{u\})\|=0$ and $\|a^+(\{u\})\|=1$ and $a^+(\{u\})=a^-(\{u\})$

The set of nodes where U-turn must be avoided is $V\setminus U$.


### Your Tasks

- Model the problem in terms of mathematical programming. You can find
  inspiration in the articles that you find in the git repository,
  especially [1,2,3,4,5,6]. The more features of the problem that you
  can model the better, but do not get stuck and if you cannot find a
  way to model some features then leave them out.

- Solve the model with the input data provided. First solve the small
  instances "Gualandi" and "BelBen" from [3] and draw their
  solutions. Then, solve the Kerteminde instance. Limit the
  computation time to max 3 hours and in case report statistics about
  the state at the time limit.

- State finally clearly whether you have solved the problem in its
  full description or some sort of relaxed version. Give the optimal
  solution or the best upper and lower bound found.
  
  

### Previous studies

Previous studies on this set of data reported a total length of the
routes to lay between an upper bound of 360.172 km and a lower bound
of 359.273 km.

If capacity constraints are not considered (hence vehicles are assumed
to have an infinite load of salt), reloading also before heading home
is neglected and U-turns are not removed, then the route found was
358.51 km long.


### References

[1] Roberto Roberti. Arc routing problems, November 2014. Slides from
DTU Transport.

[2] Ángel Corberán and Gilbert Laporte, Capacitated Arc Routing Problems, SIAM, 2014.

[3] Jose' Manuel Belenguer, Enrique Benavent, and Stefan Irnich. The
capacitated arc routing problem: Exact algotithms. In A ngel Corber
́an and Gilbert Laporte, editors, Arc routing: problems, methods, and
applications, chapter 9, pages 183–221. MOS-SIAM series on
optimization, 2014.

[4] Jose M. Belenguer and Enrique Benavent. A cutting plane algorithm
for the capacitated arc routing problem. Computers & Operations
Research, 30(5):705–728, 2003.


[5] Bruce L. Golden and Richard T. Wong, Arc Routing, Networks, Vol. 11, 1981.

[6] L. Gouveia, M. C. Mourao, and L. S. Pinto. Lower bounds for the
mixed capacitated arc routing problem. Computers & Operations
Research, 37(4):692–699, 2010.







