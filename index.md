---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: "DM872 - Mathematical Optimization at work"
layout: default
excerpt: "Main Page"
sitemap: false
permalink: /
---



### General information

- [Official course description](https://odinlister.sdu.dk/fagbesk/internkode/DM872/)

- [BlackBoard](https://e-learn.sdu.dk/webapps/blackboard/execute/courseMain?course_id=_414555_1)
  

- Teacher: [Marco Chiarandini](https://imada.sdu.dk/~marco)



### Schedule



<a href="https://mitsdu.sdu.dk/skema/activity/N340032101/f20">MitSDU</a>







### Contents



Other material for this course is available at the associated
[Git repository](https://github.com/DM872/Material)


| Week	 | Topics and Slides                                                                | 	Material                                                                                         |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           14 | [Introduction][51]. Pyomo (slides).                                              | [Intro to Python][10];  [Pyomo](http://www.pyomo.org/documentation); [Sheet 1][11]                       |
|              | Pyomo (examples).  Model Fitting (linear and non linear models).                 | [Sheet 2][12]; [Solution S.2][32]                                                                        |
|              | Installations. [Preprocessing][52].                                              | [ABGRW]                                                                                                  |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           16 | [MILP Formulations for Traveling Salesman Problem][53]                           | [Sheet 3][13]; [P] or [DFJ] or [MTZ] or [A] or [ABCC] or [OAL]                                           |
|              | Cutting Planes for TSP                                                           |                                                                                                          |
|              | More on TSP. [Network Flows duality][54]                                         | [Solution S.3][33]                                                                                       |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           17 | [Cut-and-Solve][55]                                                              | [CZ]; [Sheet 4][14]; [Solution S.4][34]                                                                  |
|              | [Modeling tricks][56]. [Timetabling][57]                                         | [KN1,KN2,ABGRW]                                                                                          |
|              | Practice                                                                         |                                                                                                          |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           18 | Timetabling                                                                      |                                                                                                          |
|              | [Timetabling][58]                                                                | [*Assignment 1*][15]                                                                                     |
|              | Practice                                                                         |                                                                                                          |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           19 | [Lagrangian Relaxation for MILP][59]                                             | [AMO ch 16];  [Fi]                                                                                       |
|              | Exercises                                                                        | [Sheet 5]({{ site.url }}{% post_url 2020-05-04-lagrangian %}); [IB]; [Fi2]; [JB]                         |
|              | Implementation, LR for TSP                                                       | [Solution S.5][35]; [Wo ch 10]                                                                           |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           20 | [Vehicle Scheduling][60]                                                         | [BCG]; [CG]                                                                                              |
|              | Exercises                                                                        | [Sheet 6]({{ site.url }}{% post_url 2019-05-15-sheet6 %})                                                |
|              | [Dantzig Wolfe decomposition][61]                                                | [AMO ch 17]; [Wo ch 11]; [LD]                                                                            |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           21 | Vehicle Routing: [Compact models][62]; [Set Partitioning formulation and CG][63] | [Fe]                                                                                                     |
|              | Vehicle Routing: [Cutting and Branching][64]                                     | [Fe]                                                                                                     |
|              | Exercises on Column Generation                                                   | [Sheet 7]({{ site.url }}{% post_url 2020-05-18-sheet7 %}) <!-- [Solutions 1][19]; [Solutions 2][20] -->  |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|
|           22 | Crew Scheduling                                                                  | <!-- [Assignment 2][16] --> <!-- [Slides][15]; [RCSP][16]; [SGSK]; [GM] -->                              |
|              | Benders Decomposition                                                            | <!-- [DJ, sec 3.5]; [Video][17] -->                                                                      |
|              | Exercises                                                                        | <!-- [Sheet 7]({{ site.url }}{% post_url 2019-05-21-sheet7 %}) -->                                       |
|--------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------|


<!--

                                                               
                                                                            


-->

<!--
[Tsp ][5]; [P] or [DFJ] or [MTZ] or [A] or [ABCC] or [OAL]
 [Sheet 1][1]; [Solutions][2];

 [Sheet 3]({{ site.url }}{% post_url 2019-04-22-sheet3 %})

<br> [Solutions][18] |
-->

<!--

| Week	 | Topics and Slides                                                            | 	Recommended reading                                                                     |   |
|--------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+---|
|           14 | MILP Languages and Solvers. MILP Formulations for Traveling Salesman Problem | [Pyomo](https://imada.sdu.dk/~marco/DM871/Training/dm545_lab_scip.pdf)                          |   |
|              | Cutting Planes for TSP                                                       |                                                                                                 |   |
|              | Exercises                                                                    | [Sheet 1][1]; [Solutions][2];                                                                   |   |
|--------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+---|
|              | 15                                                                           |                                                                                                 |   |
|              |                                                                              |                                                                                                 |   |
|--------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+---|
|           17 | Modeling Timetabling                                                         | [Timetabling][8]; [Timetabling][10]; [LL]                                                       |   |
|              | Advanced Methods for MILP                                                    | [Theory][9]; [AMO ch 15]; [Wo ch 10]                                                            |   |
|              | Exercises                                                                    | [Sheet 3]({{ site.url }}{% post_url 2019-04-22-sheet3 %})                                       |   |
|--------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+---|
|           18 | and Column Generation                                                        | [Theory][9]; [Wo ch 11]                                                                         |   |
|              | Column Generation                                                            | [Theory][9]; [Wo ch 11]                                                                         |   |
|              | Exercises on Lagrangian Relaxation                                           |                                  |   |
|--------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+---|

-->

### References


- [Py] Hart, William E., Carl D. Laird, Jean-Paul Watson, David
  L. Woodruff, Gabriel A. Hackebeil, Bethany L. Nicholson, and John
  D. Siirola. [Pyomo – Optimization Modeling in
  Python](https://www.springer.com/gp/book/9783319588193). Second
  Edition.  Vol. 67. Springer, 2017.


- [ABGRW] Tobias Achterberg, Robert E. Bixby, Zonghao Gu, Edward
  Rothberg, Dieter Weninger [Presolve Reductions in Mixed Integer
  Programming](https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/7262)
  INFORMS Journal on Computing, 2019 (accepted for publication, preprint
  available as ZIB-Report 16-44)


- [A] David L. L. Applegate, Robert E. E. Bixby, Vasek Chvátal, William
  J. J. Cook. [The traveling salesman problem: a computational
  study](https://ebookcentral.proquest.com/lib/sdub/detail.action?docID=768550).
  2006

- [ABCC] David Applegate, Robert Bixby, Vasek Chvatal, William
  Cook. [Implementing the Dantzig-Fulkerson-Johnson algorithm for large
  traveling salesman
  problems](https://www.math.uwaterloo.ca/~bico/papers/dfj_mathprog.pdf). Mathematical
  Programming, Series B. 97. 2003

- [DFJ] G. Dantzig, R. Fulkerson and S. Johnson. [Solution of a
  Large-Scale Traveling-Salesman
  Problem](https://www.jstor.org/stable/pdf/166695.pdf). Journal of the
  Operations Research Society of America, Vol. 2, No. 4 (Nov., 1954),
  pp. 393-410

- [P] Gabor Pataki. [Teaching Integer Programming Formulations Using the
  Traveling Salesman
  Problem](https://epubs.siam.org/doi/pdf/10.1137/S00361445023685)
  SIAM Review 45(1), 2003

- [MTZ] C. E. Miller, A. W. Tucker, R. A. Zemlin [Integer Programming
  Formulation of Traveling Salesman
  Problems](https://dl.acm.org/citation.cfm?id=321046)
  Journal of the ACM. 7(4), 1960


- [OAL] Temel Öncana, I. Kuban Altınelb, Gilbert Laporte. [A comparative
  analysis of several asymmetric traveling salesman problem
  formulations](https://doi.org/10.1016/j.cor.2007.11.008) Computers & Operations Research 36 (2009) 6


- [CZ] Sharlee Climer, Weixiong Zhang. Cut-and-solve: [An iterative
  search strategy for combinatorial optimization
  problems.](https://doi.org/10.1016/j.artint.2006.02.005) Artificial
  Intelligence Volume 170, Issues 8–9, June 2006, Pages 714-738


- [KN1] Ed Klotz, Alexandra M. Newman. [Practical guidelines for solving
  difficult linear
  programs](https://doi.org/10.1016/j.sorms.2012.11.001) Surveys in
  Operations Research and Management Science, 18 (1–2) (2013), pp. 1-17


- [KN2] Ed Klotz Alexandra M. Newman. [Practical guidelines for solving
  difficult mixed integer linear
  programs](https://doi.org/10.1016/j.sorms.2012.12.001) Surveys in
  Operations Research and Management Science Volume 18, Issues 1–2,
  October 2013, Pages 18-32


- [dW] D. de Werra. An introduction to timetaling. European Journal of
  Operational Research Volume 19, Issue 2, February 1985, Pages
  151-162


- [LL] G. Lach and M. Lübbecke. [Optimal University Course Timetables
  and the Partial Transversal
  Polytope](http://dx.doi.org/10.1007/978-3-540-68552-4_18). C. McGeoch
  (ed.). 7th International Workshop on Efficient and Experimental
  Algorithms (WEA08), Springer, 2008, 5038() , 235-248



- [AMO] R.K. Ahuja, T.L. Magnanti and J.B. Orlin. Network Flows: Theory,
  Algorithms, and Applications. Chapters 16 and 17 (in BB). Prentice Hall, 1993 

- [Wo] L.A. Wolsey. Integer programming. Chapters 10 and 11 (in
  BB). John Wiley & Sons, New York, USA, 1998

- [Fi] M.L. Fisher. [The Lagrangian Relaxation Method for Solving Integer
  Programming
  Problems](http://dx.doi.org/10.1287/mnsc.1040.0263). Management
  Science, 2004, 50(12), 1861-1871

- [Fi2] M.L. Fisher. [An applications oriented guide to Lagrangian
  relaxation](http://www.cs.uleth.ca/~benkoczi/OR/read/lagrange-relax-introduct-fisher85.pdf)
  Interfaces 15:2, 10-21, 1985.


- [IB] S. Ilker Birbil. [Lagrangian
  Relaxation](https://personal.eur.nl/birbil/bolbilim/teaa/02_Lag_Rel.pdf). 2016

- [JB] J. E. Beasley. [Integer Programming Solution
  Methods](http://people.brunel.ac.uk/~mastjjb/jeb/natcor_ip_rest.pdf). 


- [BCG] A.A. Bertossi, P. Carraresi and G. Gallo. [On some matching
  problems arising in vehicle scheduling
  models](http://dx.doi.org/10.1002/net.3230170303). Networks, Wiley,
  1987, 17(3), 271-281

- [CG] P. Carraresi and G. Gallo. [Network models for vehicle and crew
  scheduling](http://dx.doi.org/10.1016/0377-2217(84)90068-7). European
  Journal of Operational Research , 1984, 16(2) , 139 - 151


- [LD] M.E. Lübbecke, J. Desrosiers [Selected Topics in Column Generation](https://doi.org/10.1287/opre.1050.0234). Operations Research. Vol. 53, No. 6, 2005


- [Fe] Feillet, D. [A tutorial on column generation and branch-and-price for
  vehicle routing
  problems](https://doi.org/10.1007/s10288-010-0130-z). 4OR-Q J Oper Res
  (2010) 8: 407.



<!--

- [SGSK] I. Steinzen, V. Gintner, L. Suhl and N. Kliewer. [A Time-Space
  Network Approach for the Integrated Vehicle- and Crew-Scheduling
  Problem with Multiple
  Depots](http://dx.doi.org/10.1287/trsc.1090.0304). Transportation
  Science, 2010, 44(3), 367-382

- [GM] S. Gualandi and F. Malucelli. [Resource Constrained Shortest
  Paths with a Super Additive Objective
  Function](http://dx.doi.org/10.1007/978-3-642-33558-7_24). M. Milano
  (ed.). CP, Springer, 2012, 7514, 299-315

- [DJ] Dirickx YMI & Jennergren LP (1979). [Systems Analysis by
  Multilevel Methods: With Applications to Economics and
  Management](http://pure.iiasa.ac.at/id/eprint/1017/1/XB-79-106.pdf). Chichester,
  UK: John Wiley & Sons. ISBN 978-0-471-27626-5

-->

<!-- https://core.ac.uk/download/pdf/52942860.pdf -->



### Links:


- [Pyomo documentation](http://www.pyomo.org/documentation)

<!--
 - [RM] PySCIPOpt: Python Interface to the SCIP Optimization
   Suite. [Reference
   Manual](https://imada.sdu.dk/~marco/Misc/PySCIPOpt/index.html); [SCIP Parameters](https://scip.zib.de/doc/html/PARAMETERS.php)
-->


[10]: {{ "https://colab.research.google.com/github/DM872/Material/blob/master/Python/Python_in_a_Nutshell.ipynb" | absolute_url }}
[11]: {{ "https://github.com/DM872/Material/blob/master/sheet1/Production.ipynb" | absolute_url }}
[12]: {{ site.url }}{% post_url 2020-03-31-fitting %}
[13]: {{ "https://github.com/DM872/Material/blob/master/TSP/tsp.ipynb" | absolute_url }}
[14]: {{ site.url }}{% post_url 2020-04-20-sheet4 %}
[15]: {{ site.url }}{% post_url 2020-04-28-timetabling %}
[16]: {{ site.url }}{% post_url 2020-05-21-vrptw %}


[32]: {{ "https://github.com/DM872/Material/blob/master/sheet2/infection.ipynb" }}
[33]: {{ "https://github.com/DM872/Material/blob/master/TSP/tsp_sol.ipynb" | absolute_url }}
[34]: {{ "https://github.com/DM872/Material/blob/master/TSP/formulations_sol.ipynb" | absolute_url }}
[35]: {{ "https://github.com/DM872/Material/blob/master/Lagrange/Lagrangian.ipynb" | absolute_url }}


[51]: {{ "/assets/dm872-lec1-handout.pdf" | absolute_url }}
[52]: {{ "/assets/dm872-preprocessing-handout.pdf" | absolute_url }}
[53]: {{ "/assets/dm872-TSP_Formulations.pdf" | absolute_url }}
[54]: {{ "/assets/dm872-netflow_plus.pdf" | absolute_url }}
[55]: {{ "/assets/dm872-cut-n-solve-handout.pdf" | absolute_url }}
[56]: {{ "/assets/dm872-modeling_2-handout.pdf" | absolute_url }}
[57]: {{ "/assets/dm872-timetabling_2-handout.pdf" | absolute_url }}
[58]: {{ "/assets/dm872-timetabling_3-handout.pdf" | absolute_url }}
[59]: {{ "/assets/dm872-lagrangian-handout.pdf" | absolute_url }}
[60]: {{ "/assets/dm872-vehicle-scheduling-handout.pdf" | absolute_url }}
[61]: {{ "/assets/dm872-dantzig_wolfe-handout.pdf" | absolute_url }}

[62]: {{ "https://imada.sdu.dk/~marco/Teaching/AY2019-2020/DM872/assets/protected/02-CVRP-models.pdf" }}
[63]: {{ "https://imada.sdu.dk/~marco/Teaching/AY2019-2020/DM872/assets/protected/03-CVRP-CG.pdf" }}
[64]: {{ "https://imada.sdu.dk/~marco/Teaching/AY2019-2020/DM872/assets/protected/04-CVRP-IntegerSolutionsWithCG.pdf" }}
  

<!--

{{ "https://github.com/DM872/Material/blob/master/Python/Sheet2.ipynb" | absolute_url }}



[3]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/tsp_sol.html" | absolute_url }}
[4]: {{ "/assets/dm872-cut-n-solve-handout.pdf" | absolute_url }}
[5]: {{ "/assets/dm872-timetabling-handout.pdf" | absolute_url }}

[7]: {{ "/assets/dm872-modeling_2-handout.pdf" | absolute_url }}
[8]: {{ "/assets/dm872-preprocessing-handout.pdf" | absolute_url }}
[9]: {{ "/assets/dm872-timetabling-handout.pdf" | absolute_url }}
[10]: {{ "/assets/dm872-theory-handout.pdf" | absolute_url }}

[12]: {{ "/assets/02-CVRP-models.pdf" | absolute_url }}
[13]: {{ "/assets/03-CVRP-CG.pdf" | absolute_url }}
[14]: {{ "/assets/04-CVRP-IntegerSolutionsWithCG.pdf" | absolute_url }}

[16]: {{ "/assets/crew-scheduling.pdf" | absolute_url }}
[17]: {{ "/assets/rcsp.pdf" | absolute_url }}
[18]: {{ "https://www.youtube.com/watch?v=vQzpydNOWDY" | absolute_url }}
[19]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/Lagrangian.html" | absolute_url }}
[20]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/extended.py" | absolute_url }}
[21]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/extended_callback.py" | absolute_url }}

[13]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/tsp.html" | absolute_url }}

-->
