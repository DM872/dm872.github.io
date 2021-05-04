---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: "DM872 - Mathematical Optimization at Work"
layout: default
excerpt: "Main Page"
sitemap: false
permalink: /
---



### General information

- [Official course description](https://odinlister.sdu.dk/fagbesk/internkode/DM872/)
  
- [ItsLearning](https://sdu.itslearning.com/main.aspx?CourseID=9315)

- Teacher: [Marco Chiarandini](https://imada.sdu.dk/~marco)



### Schedule


<p>
<a href="https://mitsdu.sdu.dk/skema/activity/N340032101/f21">MitSDU</a>
</p>


<button onclick="myFunction('h1')" class="w3-btn w3-cell
w3-left-align">Overall view <i class="fa fa-caret-down"></i></button>
<div id="h1" class="w3-container w3-hide">

<div class="w3-responsive">

<div w3-include-html="./assets/dm872.html"></div>
<script>
w3.includeHTML();
</script>
</div>
</div>






### Contents




| Week | Topics and Slides                                                        | Resources                                                                    |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   14 | Introduction.                                                            | [GRB],                                                                       |
|      | LP Practical Guidelines, Interior Point Methods, Sifting                 | **[KN1]**, [HL, sc 8.4], [BGLMS, sc 3]                                       |
|      | Practice                                                                 | [Sheet 1][11]; [Sol][81]                                                     |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   15 | MILP Practical Guidelines, [Modeling][56], Presolving                    | **[KN2]**, **[ABGRW]**, **[Wi, ch7,9,10] or [GRB modeling]**                 |
|      | [MILP Formulations for Traveling Salesman Problem][53]                   | [P] or [DFJ] or [MTZ] or [A] or [ABCC] or [OAL]                              |
|      | Practice TSP                                                             | [Sheet 3][13]; [Sol][82]                                                     |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   16 | Practice on TSP                                                          | [Sheet 2][12]; [GIT]; [Sol][83]                                              |
|      | Practice on TSP                                                          |                                                                              |
|      | [Cutting Plane Algorithms for TSP][54]                                   | [DFJ], [ABCC], [OAL]                                                         |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   17 | [Lagrangian Relaxation for MILP][55]                                     | **[Fi]**                                                                     |
|      | [Lagrangian Relaxation and Linear Programming, Multicommodity Flows][56] | [Sheet 4][14]; [Sol][84] ([IB]; [JB]; [Fi2]); **[AMO ch 16 + 17.4 in LMS]**; |
|      | [Lagrangian Relaxation and Integer Programming][57]                      | [Fi, sc 8]; [AMO sc 16.4];                                                   |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   18 | [Dantzig Wolfe decomposition and Column Generation][58]                  | [BGLMS, sc 3];  **[Wo ch 11 in LMS]**; [LD]                                  |
|      | Column Generation for Multicommodity Flows                               | **[AMO ch 17.5, 17.6]**;                                                     |
|      | Practice on CG                                                           | [Sheet 5][15]                                                                |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   19 | Vehicle Routing: Compact models; Set Partitioning formulation and CG     | **[Fe]**                                                                     |
|      | Vehicle Routing: Cutting and Branching                                   |                                                                              |
|      | Exercises on Column Generation                                           |                                                                              |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   20 | Applications of LR: [Vehicle Scheduling][60]                             | [AMO sc 16.5]; [BCG]; [CG]; [Wo ch 10 in LMS]                                |
|      | Crew Scheduling; RCSP                                                    |                                                                              |
|      | Benders Decomposition                                                    |                                                                              |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|
|   21 | Timetabling                                                              |                                                                              |
|      | Timetabling                                                              |                                                                              |
|      |                                                                          |                                                                              |
|------+--------------------------------------------------------------------------+------------------------------------------------------------------------------|



### Code and Data

- [GIT] [git repository](https://github.com/DM872/Material/)





### References


- [LMS] [Our learning management system](https://sdu.itslearning.com/main.aspx?CourseID=9315)

- [KN1] Ed Klotz, Alexandra M. Newman. [Practical guidelines for solving
  difficult linear
  programs](https://doi.org/10.1016/j.sorms.2012.11.001) Surveys in
  Operations Research and Management Science, 18 (1–2) (2013), pp. 1-17

- [HL] Frederick S Hillier and Gerald J Lieberman, [Introduction to
  Operations
  Research](http://highered.mcgraw-hill.com/sites/0073376299/information_center_view0/),
  9th edition, 2010. ISBN: 0073376299

- [BGLMS] Bixby, R. E., Gregory, J. W., Lustig, I. J., Marsten, R. E.,
  & Shanno, D. F. (1992). [Very large-scale linear programming: A case
  study in combining interior point and simplex
  methods](https://scholarship.rice.edu/bitstream/handle/1911/101715/TR91-11.pdf). Technical
  Report 91-11 (Also in Operations Research, 40(5), 885.)

- [KN2] Ed Klotz Alexandra M. Newman. [Practical guidelines for solving
  difficult mixed integer linear
  programs](https://doi.org/10.1016/j.sorms.2012.12.001) Surveys in
  Operations Research and Management Science Volume 18, Issues 1–2,
  October 2013, Pages 18-32

- [ABGRW] Tobias Achterberg, Robert E. Bixby, Zonghao Gu, Edward
  Rothberg, Dieter Weninger [Presolve Reductions in Mixed Integer
  Programming](https://doi.org/10.1287/ijoc.2018.0857)
  INFORMS Journal on Computing, 32(2), 2020 (preprint available as
  [ZIB-Report
  16-44](https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/6037))
 
- [Wi] H.P. Williams. [Model building in mathematical
  programming](http://site.ebrary.com.proxy1-bib.sdu.dk:2048/lib/sdub/detail.action?docID=10657847). John
  Wiley & Sons, Chichester, Fifth Edition, 2013

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
  formulations](https://doi.org/10.1016/j.cor.2007.11.008) Computers & Operations Research 36 (2009) 


- [Fi] M.L. Fisher. [The Lagrangian Relaxation Method for Solving Integer
  Programming
  Problems](http://dx.doi.org/10.1287/mnsc.1040.0263). Management
  Science, 2004, 50(12), 1861-1871

- [Fi2] M.L. Fisher. [An applications oriented guide to Lagrangian
  relaxation](http://www.cs.uleth.ca/~benkoczi/OR/read/lagrange-relax-introduct-fisher85.pdf)
  Interfaces 15:2, 10-21, 1985.


- [AMO] R.K. Ahuja, T.L. Magnanti and J.B. Orlin. Network Flows: Theory,
  Algorithms, and Applications. Chapters 16 and 17. Prentice Hall, 1993 

- [IB] S. Ilker Birbil. [Lagrangian
  Relaxation](https://personal.eur.nl/birbil/bolbilim/teaa/02_Lag_Rel.pdf). 2016

- [JB] J. E. Beasley. [Integer Programming Solution
  Methods](http://people.brunel.ac.uk/~mastjjb/jeb/natcor_ip_rest.pdf). 

- [Wo] L.A. Wolsey. Integer programming. Chapters 10 and 11 (in
  BB). John Wiley & Sons, New York, USA, 1998

- [BCG] A.A. Bertossi, P. Carraresi and G. Gallo. [On some matching
  problems arising in vehicle scheduling
  models](http://dx.doi.org/10.1002/net.3230170303). Networks, Wiley,
  1987, 17(3), 271-281

- [CG] P. Carraresi and G. Gallo. [Network models for vehicle and crew
  scheduling](http://dx.doi.org/10.1016/0377-2217(84)90068-7). European
  Journal of Operational Research , 1984, 16(2) , 139 - 151

- [LD] M.E. Lübbecke, J. Desrosiers [Selected Topics in Column
  Generation](https://doi.org/10.1287/opre.1050.0234). Operations
  Research. Vol. 53, No. 6, 2005

- [Fe] Feillet, D. [A tutorial on column generation and branch-and-price for
  vehicle routing
  problems](https://doi.org/10.1007/s10288-010-0130-z). 4OR-Q J Oper Res
  (2010) 8: 407.




### Python



- Python tutorial from DM561: 
  - [Part 1](https://dm561.github.io/assets/dm561-lec1.pdf): basics, data types, control flow, std library, OO programming
  - [Part 2](https://dm561.github.io/assets/dm561-lec2.pdf): exceptions, file i/o, numpy
  - [Part 3](https://dm561.github.io/assets/dm561-lec3.pdf): graphics, data viz, pandas

- [P0] [Colab on Python Basics](https://colab.research.google.com/github/DM561/dm561.github.io/blob/master/assets/Python_in_a_Nutshell.ipynb)

- [GRB] Solving MILP Problems in Python with Gurobi: [Part 1](./assets/lab_gurobi_1.html); [Part 2](./assets/lab_gurobi_2.html); [Modelling 1](https://www.gurobi.com/pdfs/user-events/2017-frankfurt/Modeling-1.pdf); [Modelling 2](https://www.gurobi.com/pdfs/user-events/2017-frankfurt/Modeling-2.pdf)




### Links:

- [Pyomo](http://www.pyomo.org/)

- [RM] PySCIPOpt: Python Interface to the SCIP Optimization Suite. [Reference Manual](https://imada.sdu.dk/~marco/Misc/PySCIPOpt/index.html); [SCIP Parameters](https://scip.zib.de/doc/html/PARAMETERS.php)


<!--
[10]: {{ "https://colab.research.google.com/github/DM872/Material/blob/master/Python/Python_in_a_Nutshell.ipynb" | absolute_url }}
[11]: {{ "https://github.com/DM872/Material/blob/master/sheet1/Production.ipynb" | absolute_url }}

-->

[11]: {{ site.url }}{% post_url 2020-03-31-fitting %}
[12]: {{ "/assets/tsp_gurobi.html" | absolute_url }}
[13]: {{ site.url }}{% post_url 2021-04-15-tsp_formulations %}
[133]: {{ "https://github.com/DM872/Material/blob/master/TSP/tsp.ipynb" | absolute_url }}
[14]: {{ site.url }}{% post_url 2021-04-26-lagrangian %}
[15]: {{ site.url }}{% post_url 2021-05-02-colgen %}
[16]: {{ site.url }}{% post_url 2020-05-21-vrptw %}
[17]: {{ "https://www.youtube.com/watch?v=vQzpydNOWDY" | absolute_url }}
[18]: {{ site.url }}{% post_url 2020-04-28-timetabling %}

[81]: {{ "/assets/feat_sel.html" | absolute_url }}
[82]: {{ "/assets/formulations_sol.html" | absolute_url }}
[83]: {{ "/assets/tsp_sol.html" | absolute_url }}
[84]: {{ "/assets/Lagrangian_grp.html" | absolute_url }}


[32]: {{ "https://github.com/DM872/Material/blob/master/sheet2/infection.ipynb" }}
[33]: {{ "https://github.com/DM872/Material/blob/master/TSP/tsp_sol.ipynb" | absolute_url }}
[34]: {{ "https://github.com/DM872/Material/blob/master/TSP/formulations_sol.ipynb" | absolute_url }}
[35]: {{ "https://github.com/DM872/Material/blob/master/Lagrange/Lagrangian.ipynb" | absolute_url }}
[36]: {{ "https://github.com/DM872/Material/blob/master/VRPTW/nb/VRPTW_sol.ipynb" | absolute_url }}


[51]: {{ "/assets/dm872-lec1-handout.pdf" | absolute_url }}
[52]: {{ "/assets/dm872-preprocessing-handout.pdf" | absolute_url }}
[53]: {{ "/assets/dm872-TSP_Formulations.pdf" | absolute_url }}
[54]: {{ "/assets/TSP_210422_111820.pdf" | absolute_url }}
[55]: {{ "/assets/dm872-lagrangian-handout.pdf" | absolute_url }}
[56]: {{ "/assets/Notes_210428_114528.pdf" | absolute_url }}
[57]: {{ "/assets/Notes_210429_174511.pdf" | absolute_url }}
[58]: {{ "/assets/dm872-dantzig_wolfe-handout.pdf" | absolute_url }}

<!--

[55]: {{ "/assets/dm872-cut-n-solve-handout.pdf" | absolute_url }}
[56]: {{ "/assets/dm872-modeling_2-handout.pdf" | absolute_url }}
[57]: {{ "/assets/dm872-timetabling_2-handout.pdf" | absolute_url }}
[58]: {{ "/assets/dm872-timetabling_3-handout.pdf" | absolute_url }}
[60]: {{ "/assets/dm872-vehicle-scheduling-handout.pdf" | absolute_url }}
[61]: {{ "/assets/dm872-dantzig_wolfe-handout.pdf" | absolute_url }}
[62]: {{ "https://imada.sdu.dk/~marco/Teaching/AY2019-2020/DM872/assets/protected/02-CVRP-models.pdf" }}
[63]: {{ "https://imada.sdu.dk/~marco/Teaching/AY2019-2020/DM872/assets/protected/03-CVRP-CG.pdf" }}
[64]: {{ "https://imada.sdu.dk/~marco/Teaching/AY2019-2020/DM872/assets/protected/04-CVRP-IntegerSolutionsWithCG.pdf" }}
[65]: {{ "/assets/dm872-crew-scheduling-handout.pdf" | absolute_url }}
[66]: {{ "/assets/dm872-rcsp-handout.pdf" | absolute_url }}
[67]: {{ "/assets/dm872-drawings.pdf" | absolute_url }}




{{ "https://github.com/DM872/Material/blob/master/Python/Sheet2.ipynb" | absolute_url }}

[54]: {{ "/assets/dm872-netflow_plus.pdf" | absolute_url }}

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


[19]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/Lagrangian.html" | absolute_url }}
[20]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/extended.py" | absolute_url }}
[21]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/extended_callback.py" | absolute_url }}

[13]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/tsp.html" | absolute_url }}

-->
