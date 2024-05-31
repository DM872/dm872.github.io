---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: "DM872 (S24) -- Mathematical Optimization at Work"
layout: default
excerpt: "Main Page"
sitemap: false
permalink: /
---



### General information

- [Official course description](https://odinlister.sdu.dk/fagbesk/internkode/DM872/){:target="_blank"}
  
- [ItsLearning](https://sdu.itslearning.com/main.aspx?CourseID=31891){:target="_blank"}

- Teacher: [Marco Chiarandini](https://imada.sdu.dk/u/march){:target="_blank"}



### Schedule


<p>
<a href="https://skemaplan.sdu.dk/N340032101/f24" target="_blank">Odin</a>
<!-- <a href="https://mitsdu.sdu.dk/skema/activity/N340032101/f22">MitSDU</a> -->
</p>



<button onclick="myFunction('h1')" class="w3-btn w3-cell
w3-left-align">Overall view <i class="fa fa-caret-down"></i></button>
<div id="h1" class="w3-container w3-hide">

<div class="w3-responsive">

<div w3-include-html="./assets/dm872_h1.html"></div>
<script>
w3.includeHTML();
</script>
</div>
</div>






### Contents




| Week | Topics and Slides                                                                                  | Resources                                                              |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   14 | [Introduction][51], [Farkas][512], [Interior Point Methods][511]                                   | [GRB], [HL, sc 8.4], [MG, sc 7.2], [V, ch 21]; [NW]                    |
|      | [LP Practical Guidelines][104],  Sifting                                                           | **[KN1]**,   [BGLMS, sc 3]                                             |
|      | Practice                                                                                           | [Sheet 1][11]; [sol][81]                                               |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   15 | [MILP Practical Guidelines][105]; [Presolving][60]; [Modeling][7]                                  | **[KN2]**, *[ABGRW]*, **[Wi, ch7,9,10] or [GRB, modeling 2]**          |
|      | [MILP Formulations for Traveling Salesman Problem][144]                                            | [P] or [DFJ] or [MTZ] or [A] or [ABCC] or [OAL]; [OS] [Talk]           |
|      | Practice on TSP                                                                                    | [Sheet 2][12]; [sol][82]                                               |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   16 | [Lazy Constraints for TSP][54]                                                                     | [Sheet 3][13]; [sol][83]                                               |
|      | Rounding up the practice on TSP +  [Dantzig Wolfe decomposition and Delayed Column Generation][58] | [GIT]; [BGLMS, sc 3];  **[Wo ch 11 in LMS]**; [LD]                     |
|      | [Delayed Column Generation][599]; [Dual Bounds in Column Generation][59]                           | **[Wo ch 11 in LMS]**                                                  |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   17 | Practice on CG                                                                                     | [Sheet 4][14]; [Sol][846]                                              |
|      | Vehicle Routing: [Compact models][62]; [Set Partitioning formulation and CG][63]                   | **[Fe]**, [TV];                                                        |
|      | [Vehicle Routing: Cutting and Branching][64]; [Notes on Branching][65]                             | **[Wo sc 11.7 in LMS]**;  [C];  [Sheet 5][15]; **[Assignment 1][100]** |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   18 | [Surrogate and Lagrangian Relaxations for MILP][55]                                                | **[Wo ch 10 in LMS]**; **[Fi]**                                        |
|      | Practice on Lagrangian Relaxation                                                                  | [Sheet 6][16]; [Sol][85] **[AMO ch 16 + 17.4 in LMS]**                 |
|      | [Further Notes on Lagrangian Relaxation][57]                                                       | ([IB]; [JB]; [Fi2]); [Fi, sc 8]; [AMO sc 16.4-16.5]; [Wo ch 10 in LMS] |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   19 | Applications: [Vehicle Scheduling][66]                                                             | [BCG]; [CG]                                                            |
|      | [Crew Scheduling][67]; [RCSP][68]                                                                  | [SGSK]; [GM]; [Sheet 7][17]                                            |
|      | [Integer Programming and Heuristics][71]                                                           | **[Wo ch 13]**; **[FL]**                                               |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   20 | [Stochastic Programming][70]                                                                       | [B]; **[Wo p 241]**; [SP]                                              |
|      | [Formulating Equity and Fairness in Optimization Models][74]                                       | [CH]                                                                   |
|      | Practice on Stochastic Programming                                                                 | [Sheet 8][18]; sol in [LMS] under Resources                            |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|
|   21 | [Multiobjective optimization][75]                                                                  | [TV], [E] **[Assignment 2][101]**                                                 |
|------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------|


Further Topics out of curriculum

|   |                                                |                                                   |
|---+------------------------------------------------+---------------------------------------------------|
|   | [Benders' Algorithm][69]; [Version 2][699]     | **[Wo ch 12 in LMS]**; [DJ]; [Z];                 |
|   | Practice on Benders' Algorithm                 | [Sheet 9][19]; [Sol][86]; [Sol1][86]; [Sol2][866] |
|   | [Integer Programming and Machine Learning][73] | **[Wo sc 14.6 in LMS]**; **[BD]**; **[FJ]**       |
|---+------------------------------------------------+---------------------------------------------------|

### Code and Data

- [GIT] [git repository](https://github.com/DM872/Material/)




### References


- [LMS] [Our learning management system](https://sdu.itslearning.com/main.aspx?CourseID=31891)

- [KN1] Ed Klotz, Alexandra M. Newman. [Practical guidelines for solving
  difficult linear
  programs](https://doi.org/10.1016/j.sorms.2012.11.001) Surveys in
  Operations Research and Management Science, 18 (1–2) (2013), pp. 1-17

- [HL] Frederick S Hillier and Gerald J Lieberman, [Introduction to
  Operations
  Research](http://highered.mcgraw-hill.com/sites/0073376299/information_center_view0/),
  9th edition, 2010. ISBN: 0073376299. Extracts available in [LMS].

- [MG] J. Matousek and
  B. Gartner. [Understanding and Using Linear Programming](http://dx.doi.org/10.1007/978-3-540-30717-4). Springer
  Berlin Heidelberg, 2007

- [NW] J. Nocedal and S. J. Wright, Numerical Optimization, Second Edition. Springer Series in Operations Research, 2006.

- [V] Robert J. Vanderbei, Linear Programming: Foundations and Extensions, Fourth Edition, Springer. 2014.

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
  Rothberg, Dieter Weninger. [Presolve Reductions in Mixed Integer
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



- [AMO] R.K. Ahuja, T.L. Magnanti and J.B. Orlin. Network Flows: Theory,
  Algorithms, and Applications. Chapters 16 and 17. Prentice Hall, 1993 



- [LD] M.E. Lübbecke, J. Desrosiers [Selected Topics in Column
  Generation](https://doi.org/10.1287/opre.1050.0234). Operations
  Research. Vol. 53, No. 6, 2005

- [Fe] Feillet, D. [A tutorial on column generation and branch-and-price for
  vehicle routing
  problems](https://doi.org/10.1007/s10288-010-0130-z). 4OR-Q J Oper Res
  (2010) 8: 407.

- [Wo] L.A. Wolsey. Integer programming. John Wiley & Sons, New York, USA, 2021. Extract available from ItsLearning.


- [TV] Toth P. and Vigo D. (eds) Vehicle routing: Problems, Methods
  and Applications, Second Edition, Society for Industrial and Applied
  Mathematics, 2014
  

- [E] Matthias Ehrgott. (2005) [Multicriteria Optimization](https://doi.org/10.1007/3-540-27659-9), Second
  Edition. Springer Berlin.

<!--

- [C] J. Clausen. [Branch and Bound Algorithms-Principles and
  Examples]({{ "/assets/Clausen1999.pdf" | absolute_url
  }}). 1999. Technical Report. Department of Computer
  Science. University of Copenhagen.
-->



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

- [SGSK] I. Steinzen, V. Gintner, L. Suhl and N. Kliewer. [A Time-Space
  Network Approach for the Integrated Vehicle- and Crew-Scheduling
  Problem with Multiple
  Depots](http://dx.doi.org/10.1287/trsc.1090.0304). Transportation
  Science, 2010, 44(3), 367-382

- [GM] S. Gualandi and F. Malucelli. [Resource Constrained Shortest
  Paths with a Super Additive Objective
  Function](http://dx.doi.org/10.1007/978-3-642-33558-7_24). M. Milano
  (ed.). CP, Springer, 2012, 7514, 299-315
 
- [FL] M. Fischetti, A. Lodi, [Heuristics in Mixed Integer
  Programming](https://homepages.cwi.nl/~dadush/workshop/discrepancy-ip/papers/heuristics-survey-fischetti-lodi-11.pdf),
  Wiley Encyclopedia of Operations Research and Management Science
  (James J. Cochran ed.), John Wiley & Sons, Vol. 8, 738-747, 2011.

- [B] John E Beasley [Stochastic
  Programming](people.brunel.ac.uk/~mastjjb/jeb/or/sp.html) in OR-Notes

- [CH] Violet (Xinying) Chen and J. N. Hooker. [A Guide to Formulating
  Equity and Fairness in an Optimization
  Model](http://public.tepper.cmu.edu/jnh/equityGuideAOR.pdf). [Video](https://cp2021.lirmm.fr/submissions/2001)

- [TV] Satya Tamby, Daniel Vanderpooten. (2021) [Enumeration of the
  Nondominated Set of Multiobjective Discrete Optimization
  Problems](https://doi.org/10.1287/ijoc.2020.0953). INFORMS Journal on
  Computing 33(1):72-85



- [DJ] Dirickx YMI & Jennergren LP (1979). [Systems Analysis by
  Multilevel Methods: With Applications to Economics and
  Management](http://pure.iiasa.ac.at/id/eprint/1017/1/XB-79-106.pdf). Chichester,
  UK: John Wiley & Sons. ISBN 978-0-471-27626-5


- [Z] Zhang, Ray Jian, [Benders Decomposition: An Easy Example](https://youtu.be/vQzpydNOWDY). 2016. Video


- [BD] Bertsimas, D. and Dunn, J. (2017). [Optimal classification
  trees](https://dx.doi.org/10.1007/s10994-017-5633-9). Machine
  Learning 106(7): 1039–1082.

- [BD2] Bertsimas, D. and Dunn, J. (2019). Machine Learning Under a
  Moden Optimization Lens. Dynamic Ideas LLC.

- [FJ] Fischetti, M. and Jo, J. (2018). [Deep neural networks and
  mixed integer linear
  optimization](https://doi.org/10.1007/s10601-018-9285-6). Constraints
  23: 296–309.





### Python


- See Tutorials "Python Review" and "MILP Software" in [DM871](https://dm871.github.io/)

<!--
- Python tutorial from DM561: 
  - [Part 1](https://dm561.github.io/assets/dm561-lec1.pdf): basics, data types, control flow, std library, OO programming
  - [Part 2](https://dm561.github.io/assets/dm561-lec2.pdf): exceptions, file i/o, numpy
  - [Part 3](https://dm561.github.io/assets/dm561-lec3.pdf): graphics, data viz, pandas

- [P0] [Colab on Python Basics](https://colab.research.google.com/github/DM561/dm561.github.io/blob/master/assets/Python_in_a_Nutshell.ipynb)
-->


- [GRB] Solving MILP Problems in Python with Gurobi: [Modelling 1](https://www.gurobi.com/pdfs/user-events/2017-frankfurt/Modeling-1.pdf); [Modelling 2](https://www.gurobi.com/pdfs/user-events/2017-frankfurt/Modeling-2.pdf);
[Algorithms 1](https://assets.gurobi.com/pdfs/user-events/2017-frankfurt/Algorithms-I.pdf);
[Algorithms 2](https://assets.gurobi.com/pdfs/user-events/2017-frankfurt/Algorithms-II.pdf)



### Links

- [OS] [Optimization Software: links to solvers and benachmarks](https://imada.sdu.dk/u/march/Blog/optimization/software/2023/02/12/optsoft.html)


- [SP] [Stochastic Programming Society](https://www.stoprog.org/)




<!--
### Videos
- [Talk] [The Traveling Salesman Problem](https://www.youtube.com/live/Mpj8vo18W1E?feature=share) public lecture by William Cook on May 3rd 2023 at LSE.
-->

### Assessment

- Ordinary exam: two assignments during the course

- Reexam: assignments in August 2024





<!--
[10]: {{ "https://colab.research.google.com/github/DM872/Material/blob/master/Python/Python_in_a_Nutshell.ipynb" | absolute_url }}
[11]: {{ "https://github.com/DM872/Material/blob/master/sheet1/Production.ipynb" | absolute_url }}

-->

[11]: {{ site.baseurl }}{% post_url 2020-03-31-fitting %}
[12]: {{ "/assets/tsp_formulations_gurobi.html" | absolute_url }}
[82]: {{ "/assets/formulations_sol.html" | absolute_url }}
<!-- [13]: {{ site.baseurl }}{% post_url 2021-04-15-tsp_formulations %} -->
[13]: {{ "/assets/tsp_gurobi.html" | absolute_url }}
[83]: {{ "/assets/tsp_sol_gurobi.html" | absolute_url }}

[84]: {{ "https://github.com/demirayonur/Column-Generation/blob/main/ColumnGeneration_CuttingStockProblem.ipynb" }}
[844]: {{ "/assets/Notes_220427_155254.pdf" | absolute_url }}
[845]: {{ "https://github.com/DM872/Material/blob/main/BinPacking/extensive.py" }}

[133]: {{ "https://github.com/DM872/Material/blob/master/TSP/tsp.ipynb" | absolute_url }}
[14]: {{ "/sheets/delcolgen.html" | absolute_url }}
[846]: {{ "/sheets/delcolgen_sol.html" | absolute_url }}
[15]: {{ "/sheets/bnprice.html" | absolute_url }}
[16]: {{ "/sheets/lagrangian.html" | absolute_url }}
[17]: {{ "/sheets/vehicle_sch.html" | absolute_url }}
[18]: {{ "/sheets/stoch.html" | absolute_url }}
[19]: {{ "/sheets/benders.html" | absolute_url }}



[81]: {{ "/assets/feat_sel.html" | absolute_url }}
[85]: {{ "/sheets/lagrangian_sol.html" | absolute_url }}

[86]: {{ "/assets/benders_example.html" | absolute_url }}
[866]: {{ "https://github.com/DM872/Material/blob/master/Benders/benders_example_2.ipynb" | absolute_url }}


[32]: {{ "https://github.com/DM872/Material/blob/master/sheet2/infection.ipynb" }}
[33]: {{ "https://github.com/DM872/Material/blob/master/TSP/tsp_sol.ipynb" | absolute_url }}
[34]: {{ "https://github.com/DM872/Material/blob/master/TSP/formulations_sol.ipynb" | absolute_url }}
[35]: {{ "https://github.com/DM872/Material/blob/master/Lagrange/Lagrangian.ipynb" | absolute_url }}
[36]: {{ "https://github.com/DM872/Material/blob/master/VRPTW/nb/VRPTW_sol.ipynb" | absolute_url }}


[7]: {{ "/assets/dm872-slides-modeling_2.pdf" | absolute_url }}
[51]: {{ "/assets/dm872-slides-lec1.pdf" | absolute_url }}
[511]: {{ "/assets/dm872-slides-interior.pdf" | absolute_url }}
[512]: {{ "/assets/dm872-slides-farkas.pdf" | absolute_url }}
[52]: {{ "/assets/dm872-slides-preprocessing.pdf" | absolute_url }}

[144]: {{ "/assets/dm872-slides-tsp.pdf" | absolute_url }}
[53]: {{ "/assets/dm872-TSP_Formulations.pdf" | absolute_url }}
[54]: {{ "/assets/TSP_210422_111820.pdf" | absolute_url }}

[55]: {{ "/assets/dm872-slides-lagrangian.pdf" | absolute_url }}
[56]: {{ "/assets/Notes_210428_114528.pdf" | absolute_url }}
[57]: {{ "/assets/Notes_230509_110632.pdf" | absolute_url }}
[577]: {{ "https://scipbook.readthedocs.io/en/latest/bpp.html" }}
[58]: {{ "/assets/dm872-slides-dantzig_wolfe.pdf" | absolute_url }}
[59]: {{ "/assets/Notes_220425_163727.pdf" | absolute_url }}
[599]: {{ "/assets/dm872-slides-solving_lmp.pdf" | absolute_url }}
[60]: {{ "/assets/dm872-preprocessing-handout.pdf" | absolute_url }}

[62]: {{ "https://sdu.itslearning.com/LearningToolElement/ViewLearningToolElement.aspx?LearningToolElementId=1471369" }}
[63]: {{ "https://sdu.itslearning.com/LearningToolElement/ViewLearningToolElement.aspx?LearningToolElementId=1471370" }}
[64]: {{ "https://sdu.itslearning.com/LearningToolElement/ViewLearningToolElement.aspx?LearningToolElementId=1471371" }}
[65]: {{ "/assets/Notes_210513_112748.pdf" | absolute_url }}

[66]: {{ "/assets/dm872-slides-vehicle-scheduling.pdf" | absolute_url }}
[67]: {{ "/assets/dm872-slides-crew-scheduling.pdf" | absolute_url }}
[68]: {{ "/assets/dm872-rcsp-handout.pdf" | absolute_url }}
[69]: {{ "/assets/Notes_230515_095251.pdf" | absolute_url }}
[699]: {{ "/assets/Notes_230516_122803.pdf" | absolute_url }}
[70]: {{ "/assets/dm872-slides-stochastic.pdf" | absolute_url }}
[71]: {{ "/assets/dm872-slides-cut-n-solve.pdf" | absolute_url }}
[72]: {{ "/assets/Notes_230523_124056.pdf" | absolute_url }}
[73]: {{ "/assets/dm872-slides-ml.pdf" | absolute_url }}
[74]: {{ "/assets/dm872-slides-fairness.pdf" | absolute_url }}
[75]: {{ "/assets/dm872-slides-multiobj.pdf" | absolute_url }}

[100]: {{ "/assignments/vrptw.html" | absolute_url  }}
[101]: {{ "/assignments/exams.html" | absolute_url  }}
[103]: {{ site.baseurl }}{% post_url 2021-05-28-salt_spreading %}
[102]: {{ "/assets/kkt.pdf" | absolute_url  }}
[108]: {{ site.baseurl }}{% post_url 2022-05-30-exams %}
[109]: {{ "/assignments/timetabling.html" | absolute_url }}

[104]: {{ "https://docs.google.com/presentation/d/1b6FRSO-KjgBJxeybW63oW3dBznAQxJ66HP0WHXTgsxY/edit?usp=sharing" }}
[105]: {{ "https://docs.google.com/presentation/d/13UPVjMRNn524ej_-cPFZS1CWzPlMs1HxkhdyfWVJrro/edit?usp=sharing" }}


[110]: {{ "/assets/dm872-interior.pdf" | absolute_url }}

<!--
[104]: {{ "/assets/dm872-guidelines_lp.pdf" | absolute_url  }}
[105]: {{ "/assets/dm872-guidelines_milp.pdf" | absolute_url  }}
-->

<!--
[55]: {{ "/assets/dm872-cut-n-solve-handout.pdf" | absolute_url }}
[56]: {{ "/assets/dm872-modeling_2-handout.pdf" | absolute_url }}
[57]: {{ "/assets/dm872-timetabling_2-handout.pdf" | absolute_url }}
[58]: {{ "/assets/dm872-timetabling_3-handout.pdf" | absolute_url }}


[61]: {{ "/assets/dm872-dantzig_wolfe-handout.pdf" | absolute_url }}
[67]: {{ "/assets/dm872-drawings.pdf" | absolute_url }}



[66]: {{ "https://github.com/DM872/Material/blob/master/Python/Sheet2.ipynb" | absolute_url }}

[54]: {{ "/assets/dm872-netflow_plus.pdf" | absolute_url }}

[3]: {{ "https://www.imada.sdu.dk/~marco/Teaching/AY2018-2019/DM872/assets/tsp_sol.html" | absolute_url }}
[4]: {{ "/assets/dm872-cut-n-solve-handout.pdf" | absolute_url }}
[5]: {{ "/assets/dm872-timetabling-handout.pdf" | absolute_url }}



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
