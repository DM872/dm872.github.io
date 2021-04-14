---
layout: default
mathjax: true
title:  Sheet 4
date:   2021-04-14 09:33:19 +0100
categories: exercises 
---

## Sheet 3


### Task 1  -  Home Preparation


Beside the DFJ formulation with cutting plane procedure there are
other formulations for the TSP that we saw in class and that have a
polynomial number of constraints:

- the MTZ formulation (C. E. Miller, A. W. Tucker, and R. A. Zemlin,
“Integer programming formulations and traveling salesman problems,” J.
ACM, 7 (1960), pp. 326–329)

- the Flow with Gain by Svestka (JA Svestka, "A continuous variable representation of the TSP," Math Prog, v15, 1978, pp 211-213)

- the step model by Dantzig ("Linear Programming and Extensions" 1963, Dantzig G.B.)


Your task:


+ Argue that the formulations are correct for the traveling salesman
problem, that is, show that a solution to the traveling salesman
satisfies all constraints given and that a solution with subtours
would be ruled out by the formulation.


+ Solve the instance on the 20 random nodes with the formulations
given keeping the integrality requirement for the main variables so
that the optimal solution can be found. Which formulation is the
fastest to solve the problem? How many branch and bound nodes are
needed in each formulation to find the optimal solution?


+ Compare the DFJ and MTZ formulations on the basis of the quality of
their linear relaxations on the instance with random points and on the
instances `dantzig42`, `berlin52.dat`, `bier127.dat`. Can they all
solve these instances?  Which formulation provides the tigthest LP
relaxation?


+ Experiment ideas to solve the instance. For example, try combining
the DFJ formulation with one of those here.




<!---

### Task 2  -  In Class: Cut and Solve

Study the paper on Cut and Solve [CZ]. Implement the cut and solve
method for the traveling salesman problem using the DFJ formulation as
done in that paper. Compare the results with the optimal solutions
from the DFJ and MTZ formulations without cut and solve.

--->
