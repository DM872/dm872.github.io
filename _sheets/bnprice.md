---
layout: default
mathjax: true
title:  Sheet 5
date:   2022-05-04 09:33:19 +0100
categories: exercises 
---

## Sheet 5



In Task 3 of Sheet 4, we were lucky for the examples tested that the
heuristic solution of the FFD algorithm was proven optimal by the lower
bound found solving the LMP. When that is not the case we need to
continue by branch-and-price or branch-and-cut-and-price. Design a
branch-and-price algorithm for your extensive formulation of the bin
packing problem developed in Sheet 4.  You can use as a reference the
skeleton given on page 121 pf [Wo] and define the branching scheme and
its implications on the pricing problem. You can try to perform the
branch-and-price by hand using the methods implemented in the previous
sheet (ignoring the result of the FFD heuristic).

Implementations:

- gurobi does not provide support for variable addition at the nodes of
the solver branch and bound via callback. Hence, using
gurobi you would need to reimplement the whole branch and bound
algorithm solving from scrtach a column generation at every node of the
tree.


- pyscipopt provides support by defining a class inherited from
`Pricer`. The script `test_pricing.py` from the pyscipopt github
repository shows how to do this. 




### Solution

For a discussion on a solution approach see: 

J M Valerio de Carvalho. "Exact solution of bin-packing problems using
column generation and branch-and-bound" *Annals of Operations Research*
1999; 86, pg. 629


See also:

François Vanderbeck. Branching in branch-and-price: a generic scheme
Math. Program., Ser. A (2011)
130:249–294. https://dx.doi.org/10.1007/s10107-009-0334-1


