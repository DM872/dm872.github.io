---
layout: default
mathjax: true
title:  Assignment 1
date:   2023-04-30 08:33:19 +0100
categories: assignments 
---

**Deadline: Monday, May 22 at 11:59 am.** 

<!--
For questions on the assignment, use the [Discussion Board in the
LMS](https://sdu.itslearning.com/ContentArea/ContentArea.aspx?LocationID=17799&LocationType=1).
-->

## Assignment 1

This assignment will be graded and will contribute to your final
assessment in the course. Overall there will be two assignments.

The assignment has to be carried out individually.

To complete the assignment you have to submit in [LMS] a `.tgz` or `.zip` archive
named `asg1.tgz` or `asg1.zip` that decompress in the following
structure:
```
asg1
|
+--tex
+--src
```

- `tex` must contain a report in pdf format as concise as possible (by no way more than 10
  pages) with the answers to the tasks. The report should be written
  preferably in Latex using this [template]({{ "/assets/template_answers.tex" | absolute_url }}).

- `src` must contain the Python code for the calculations.






#### Problem Description

This assignment is proposed by courtesy of Roberto Roberti. The *Vehicle
Routing Problem with Time Windows* (VRPTW) is a generalization of the
Capacitated Vehicle Routing Problem (CVRP), where
each customer must be visited within a given time window.

The VRPTW can be stated as follows. A directed graph $G = (V, A)$ is
given, where $V$ is the set of vertices and $A$ is the set of
arcs. The set of vertices $V$ is defined as $V = N \cup \\left\\{o,
d\\right\\}$, where $N = \\left\\{1, 2, . . . , n\\right\\}$ is a set
of $n$ customers and $o$ and $d$ represent the start and the end point
of each route (in practice, $o$ and $d$ represent the same depot but
are kept separate for notational purposes). The set of arcs $A$ is
defined as $A = \\left\\{(i, j) : i, j \in V, i \neq j\\right\\}$; a travel cost
$c_{ij}$ and a travel time $t_{ij}$ are associated with each arc $(i,
j) \in A$.


Each customer $i \in N$ requests $q_i$ units of a given commodity and
can be visited only within a given time window $[e_i, l_i]$, where $e_i$
and $l_i$ are the earliest and the latest time to serve customer $i$;
nonetheless, a vehicle is allowed to arrive at $i$ before $e_i$, but, in
this case, the service starts at $e_i$. A set $K = \\left\\{1, 2, . . . , m\\right\\}$
of $m$ vehicles can be used to serve the customers; each vehicle has
capacity $Q$.  


The goal of the VRPTW is to find a set of routes of minimum total cost
to assign to the vehicles, such that
- No more than $m$ routes are selected; 
- Each route starts from $o$ within the depot time window, visits a set
of customers, each within its time window, whose total requests do not
exceed $Q$, and ends at $d$ within the depot time window; 
- Each customer is visited by exactly one of the routes.  


You are given a VRPTW instance in Python code at the end of this
document. The layout of the customers is as follows:


![instance]({{ "/assets/images/vrptw_instance.png" | absolute_url }}){: .center-image }


It can be helpful adapting the utilities used for the TSP exercises to
plot your solutions.


#### Task 1: Set Partitioning Formulation

Describe how the VRPTW can be formulated as a Set Partitioning (SP)
problem.

As usual, to describe a model you have at least to:

- introduce the notation
- write the full mathematical model
- explain every row of the model justifying why it is a correct model of the problem at hand.

An analysis of the model from a computational point of view is a plus.



#### Task 2: Heuristic Solution

Find a heuristic solution of the given instance and describe it.

Keep the heuristic simple both implementation-wise and
computationally. A feasible solution is enough. Avoid finding the
optimal solution with the heuristic.  You can describe the procedure in
a few lines and maybe present the picture of the obtained routes
together with calculating and reporting the cost/quality of the
solution.


#### Task 3: Pricing Problem Formulation

Describe the Master Problem (MP) and the Restricted Master Problem (RMP)
derived from the SP formulation, present and describe a mathematical
formulation of the resulting pricing problem.


#### Task 4: Column Generation by Hand

Starting from the columns defined in the data below, solve the master
problem by finding by "manual inspection" and adding additional columns
to the datafile. You can use a solver for the solution of the restricted
linear master problem but you must identify promising columns by hand
and justify your choice.

<s>
Report in a plot the behaviour of the best dual bound available during
the column generation process.
</s>

(It is not so important to prove optimality here, you will do that in
 the next task.)
 
#### Task 5: Describe and Implement a Column Generation Procedure for the VRPTW

Starting from the provided data below and a template for column
generation delivered during the course (the bin packing example),
implement in Pyhton a Column Generation procedure, computing an optimal
solution to the linear relaxation of the master problem, by adding the
route having the most negative reduced cost, at every iteration. As the
initial columns, use the ones provided in the data below. Describe, in
details the different steps implied by the Column Generation Procedure
and report a plot that shows the trend of the value of the pricing
problem and the derived dual bound to the master problem.


[To add columns to your model without resolving from scratch see the
last example from this doumentation page:
[Modify a model (gurobi.com)](https://www.gurobi.com/documentation/10.0/examples/modify_a_model.html).]


#### Task 6: Cutting

If the optimal MP solution you achieved in Task 4 is fractional, add
Subset-Row inequalities to RMP and resolve using column
generation. Continue adding cuts until no more violated cuts can be
found. Describe the process in detail, and comment on the results.  You
can either do this manually (similar to Task 4), or by implementing it
in the code. 


#### Task 7: Branching 

If the optimal MP solution you achieved in Task 4 is fractional, find an
optimal SP solution by generating a branch-and-bound tree. Describe the
process in detail, visualise the branch-and- bound tree, and comment on
the results.  You can either do this manually (similar to Task 4), or by
implementing it in the code.


#### Data and Code


```python
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

class data: 
    cust = 8 #Number of customers
    m = 3 #Maximum number of vehicles
    Q = 10 #Maximum vehicle capacity

    demand = array([4,  3,  3,   3,   3,  4,  3,  3  ]) #demand per customer
    twStart = array([0,  6,  8,  4,   6,   5,  6,  5,  4,  0]) #earlierst delivery time
    twEnd   = array([24, 6,  16, 20,  6,  19, 18, 19, 6, 24]) #latest delivery time


    # Travel cost matrix
    cost = array([
        [0,  7,  5,  3,  3,  4,  5,  4,  3,  0],
        [7,  0,  3,  5,  4, 11, 12, 10, 10,  7],
        [5,  3,  0,  5,  2,  9,  9,  8,  9,  5],
        [3,  5,  5,  0,  4,  6,  8,  7,  5,  3],
        [3,  4,  2,  4,  0,  6,  7,  6,  6,  3],
        [4, 11,  9,  6,  6,  0,  2,  2,  2,  4],
        [5, 12,  9,  8,  7,  2,  0,  1,  4,  5],
        [4, 10,  8,  7,  6,  2,  1,  0,  4,  4],
        [3, 10,  9,  5,  6,  2,  4,  4,  0,  3],
        [0,  7,  5,  3,  3,  4,  5,  4,  3,  0]
        ])
    
    #Travel time matrix
    timeCost = array([
        [0,  6,  6,  4,  4,  5,  6,  5,  4,  0],
        [6,  0,  4,  6,  5, 12, 13, 11, 11,  6],
        [6,  4,  0,  6,  3, 10, 10,  9, 10,  6],
        [4,  6,  6,  0,  5,  7,  9,  8,  6,  4],
        [4,  5,  3,  5,  0,  7,  8,  7,  7,  4],
        [5, 12, 10,  7,  7,  0,  3,  3,  3,  5],
        [6, 13, 10,  9,  8,  3,  0,  2,  5,  6],
        [5, 11,  9,  8,  7,  3,  2,  0,  5,  5],
        [4, 11, 10,  6,  7,  3,  5,  5,  0,  4],
        [0,  6,  6,  4,  4,  5,  6,  5,  4,  0]
        ])
  
    #The initial routes for Task 4 and 5
    #Each row describe the customers visited in a route. If the n'th index in a row is '1.0', then the route visits customer n.
    routes = array([
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1]
    ])

    #The distance cost of the initial routes.
    costRoutes = array([15.0, 12.0, 22.0, 18.0, 15.0, 22.0, 18.0, 10.0, 15.0, 11.0, 13.0, 12.0])

    #For Task 5. Input the routes you found in Task 2
    routes = array([[]])
    costRoutes = array([])


    nodes = [(3.5,3.5),(0,0),(0,2),(3.5,1.5),(1,2.5),(5,5),(4,6.5),(3.5,5.5),(6,4)]
    labels = list(range(9))

    @staticmethod
    def plot_points(outputfile_name=None):
        "Plot instance points."
        style='bo'
        plt.plot([node[0] for node in data.nodes], [node[1] for node in data.nodes], style)
        plt.plot([data.nodes[0][0]], [data.nodes[0][1]], "rs")
        for (p, node) in enumerate(data.nodes):
            plt.text(node[0], node[1], '  '+str(data.labels[p]))
        plt.axis('scaled'); plt.axis('off')
        if outputfile_name is None:
            plt.show()
        else:
            plt.savefig(outputfile_name)

    @staticmethod
    def plot_routes(points, style='bo-'):
        "Plot lines to connect a series of points."
        for route in points:
            plt.plot(list(map(lambda p: data.nodes[p][0], route)), list(map(lambda p: data.nodes[p][1], route)), style)
        data.plot_points()


if __name__ == "__main__":
    data.plot_points()
    data.plot_routes([[0,1,2,3,0],[0,4,0],[0,7,6,5,8,0]])
```


#### Question and Answers


Q: If one has a hard time doing the 4th task, are we then doomed to fail since both task 5, 6 and 7 depends on this task alone?

A: No, you are not doomed to fail if you do task 5, 6 and 7 correct. The
goal of Task 4 is only to help you to make sure that you have understood
how to calculate the value of tentative columns.


Q: What should I do in Task 6 and 7 if the optimal MP solution I achieved in Task 4 was not fractional.

A: You should revise Task 5 becausedoing that right would allow you to
discover that the optimal solution in Task 4 is fractional.


Q: I am having trouble finding an efficient Cut Separation Problem for
finding the most violated cuts of my LP solutions to the VRPTW
instance. Since the instance is rather small one way would simply be to
bruteforce it, but a more efficient approach I am having trouble
finding. Is it possible to get a hint on a more efficient approach?

A: We did not look at cut separation procedures for SR cuts. If you want
you can try to formuate the problem but it is not what is asked in the
task. Manual or exhaustive procedures as you mention are ok for this
assignment.  You can find a procedure in this paper: “Subset-Row
Inequalities Applied to the Vehicle-Routing Problem with Time Windows”
by Mads Jepsen, Bjørn Petersen, Simon Spoorendonk and David Pisinger
