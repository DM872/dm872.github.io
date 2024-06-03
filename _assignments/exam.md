---
layout: assignment_plain
title:  "Assignment 2"
date: 2024-05-24 11:00:00 +0100
date_show: 2024-05-23 08:27:19 +0100
mathjax: true
week: 22
sol_url: ""
comments: true
categories: assignments
---


# Obligatory Assignment 2

## Preamble
 
- This is the second of two obligatory assignments. This assignment will be graded and will contribute to your final
  assessment in DM872. 

- The assignment has to be carried out individually.

- To complete the assignment you have to submit in ItsLearning a pdf document and a `.tgz` or `.zip` archive
  named `asg2.tgz` or `asg2.zip`. 

    - The pdf file must contain the report as concise as possible (by no way more than 10
    pages) with the answers to the tasks. The report should be written
    preferably in Latex using this [template]({{ "/assets/template_answers.tex" | absolute_url }}).

    - The archive must decompress in the following structure:
        ```
        asg2
        |
        +--src
        ```
        `src` must contain the Python code for the calculations.

- **Deadline: Wednesday, June 28, 2024, at noon** 

- The case proposed is examination timetabling. The case is left quite
  open for different approaches. It is also possible to work on a case
  of own choice but this has to be agreed with the teacher in due time.

- Changes made to this document after May 31 will be shown in a
  different color.



## Exam Timetabling 

You have to use Mathematical Programming to schedule the exams at the Faculty
of Science at SDU.

A starting package for the implementation is available in the course git repository [GIT]. The description of the instances has been moved
there in the `README.md` file of the `data/` directory.

Let $E$ be the set of exams for courses that need to have a date
scheduled. Let $D$ be the set of days and $R$ the set of rooms that are
available for scheduling exams. Each exam $e$ from $E$ has a set of
enrolled students $S_e$ and requires a number of days depending on
whether it is written or oral.

Exams that for some reason cannot have overlapping schedules are
called *conflicting* exams. In particular, exams with the same teacher
or censor and exams that belong to the same study program are considered
conflicting. For an exam $i$ from $E$ the set of conflicting exams is denoted $C_i$.

Exams may share students. The number of students each pair of courses share is denoted by $s_{ij}$ in $\mathbb{Z}_0^+$ for $i,j$ in $E$.

Further, exams may be $joined$, that is, they need to have the same starting date. For an exam $i$ from $E$, the set of exams that must be "joined" with it is denoted $J_i$.  

An *exam schedule* is an assignment of exams to days and rooms, that
is, it is a function $\sigma : E \to 2^{D\times R}$. For example, an exam $i$ scheduled in days $1$ and $2$ in rooms $a$ and $b$, respectively, can be represented by $\sigma: i \mapsto \\{(1,a),(2,b)\\}$. An exam schedule is
*feasible* if it satisfies the following constraints:

1.  Each exam in input is scheduled to start and finish in the days
    available.

2.  Each exam is assigned a number of days equal to the
    number of required days to carry out the exam.

3.  Exams with exam duration more than one day receive consecutive days.
    No holes due to weekend or holidays are allowed within an exam
    schedule.

4.  <s>Exams with preassigned dates and rooms must respect those preassignments and need not necessarily to satisfy the previous three constraints.
    If present, preassignments are specified in the field `schedule` of each exam.</s>

5.  Exams that are *joined* must have schedules starting on the same
    day. (The duration for both should be the sum of the duration of the
    two exams but you can ignore this).

6.  Exams that are *conflicting* must be scheduled in sets of days with
    empty intersection.

7. *Written* exams (`type=='s'`) must be scheduled in rooms with enough capacity (`seats`) to accommodate all the students registered to the exams (ideally, there should be a capacity reduction factor to ensure enough distance between students but we will ignore this here, or assume the reduction has already been done).

8. *Oral* exams (`type=='m'`) must be scheduled in rooms with capacity less than 10.

9.  **Optional:** *Room stability.* Exams with duration longer than one day, e.g. oral exams, are scheduled all days in the same room.

<!--
9.  The total number of students having *written* exams in a day must be
    smaller than `MAX_SEATS_PER_DAY`. Exams with preassigned dates do not
    contribute to this constraint. (This constraint must be relaxed on the reexam instances.)

10. The total number of *oral* exams in a day must be smaller than
    `MAX_ROOMS_PER_DAY` in order to ensure that a room to host them can
    be found. Exams with preassigned dates do not count in this
    constraint.
-->





If a schedule that satisfies all the above constraints is found, then
one must maximize the distance between the starting times of exams that
share students ($s_{ij}>0$) (weekends should be counted in the distance
as working days). This optimization task can be achieved in different
ways and it is up to you modeling this aspect. It is also desirable
finding solutions that address some definition of fairness.

<!--
 , for example, by introducing a new constraint
that enforces a distance of at least $R$ days between exams that share students
and then maximizing $R$ and/or minimizing the number of students
violating this constraints, or by devising a penalty scheme that
penalizes exams sharing students that are scheduled too close.

If a feasible schedule cannot be found, then one must relax the
constraints on the conflicting courses and treat them as those sharing
students but with higher priority in avoiding overlaps. In this case,
the parameter `WEIGHT_PROGRAMS` can be used to indicate the relative
importance between avoiding overlaps for conflicting courses and
avoiding overlaps for courses that only share students.
-->

### Your Task (Deterministic Case)

Formulate the problem in MILP terms, implement the model and solve the instances of the problems made available for E23. 




### Stochastic elements

During the scheduling process rooms can change their status, from available to unavailable. Hence, the availability of a room is a stochastic variable. 
If an exam is scheduled in a room that becomes unavailable one of two repair actions must be undertaken: i) moving the exam to another room with enough capacity without changing the days; ii) rescheduling the exam to different day(s) and room(s). We can assume that action i) has no cost. Action ii) has instead a cost and we would like to minimize it. The presence of the optional constraint about room stability may increase the need for actions ii). It is up to you whether to include or not this optional but realistic constraint. 


Rather than through a theoretical expression, we approximate the description of the random variables for the room availability through a finite number of
future scenarios of room availability, each scenario occurring with equal probability.




### Your Task (Stochastic Case)

Formulate the problem as a stochastic programming problem using one of the techniques seen in class, implement the model and solve the instances of the problems made available for E23. 


### Remarks


- There is no predefined time limit for your experiments. You can choose
  to run your experiments with the time limit that best fits with your
  computational resources (eg, time left from deadline, number of cores
  and machines, etc). Performance can be assessed in several ways (max
  size of the instances solved, computation time, solution quality,
  etc.)  It is up to you to identify meaningful measures and comment on
  the performance.





### Input Data

In your git repository you will find input instances for E23. You should
start experimenting with the smallest instances and grow to the largest.

In the following table for each instance it is given in the order: the
number of exams, the number of exam days to allocate, the number of room
days available and the number of students.

```
|         | exams | exam days | students |
|---------+-------+-----------+----------|
| sund    |     9 |        17 |      285 |
| biologi |    14 |        17 |      210 |
| bmb     |    21 |        22 |      592 |
| samf    |    24 |        33 |      581 |
| fkf     |    51 |        59 |      692 |
| imada   |    60 |       101 |      861 |
| all     |   179 |       249 |     2428 |
```



The starting package implements the reading of the instances and
generation of scenarios for the stochastic case. Some preprocessing
occurs during reading. For example, in the data files there are also
exams without students or with types "o" or "u". These exams are removed
while reading the instances, hence you do not have to worry about them.

To execute the starting package run: 

```
python3 src/main.py data/E23/biologi.json -o output_dir
```

In the package there is also a verifier for the constraints of the
problem.

```
python ../src/verifier.py -a F23/solution.json F23/all.json -o .
```

At the time of writing the verifier must be updated to handle also
rooms.


Important: there might come updates to the files of the starting
package, hence you should not modify them. Importing them in your code
should be safe.

<p style="color:blue;">
The data you will need are:

- `instance.config` a dictionary containins `days`, a list of days available for scheduling exams

- `instance.exams` a dictionary of exams containing deatils for each exams, including the number of days required and the type `s`, `m`. 

- `instance.room_scenarios` a dictionary with keys the number of scenario. Then for each scenario a dictionary with keys the days and values a list of avaialble rooms. Use `instance.room_capacity(room_id)` to find the capacity of each room. Use `instance.room_scenarios[0]` for the deterministic case. Do not use instance.room_details.

- `instance.shared` a dictionary with keys the pairs of exams and values the list of shared students 

- `instance.adj` a dictionary with keys the pairs of exams and values the number of shared students 

</p>


### Output Format 

The output file contains a solution in json format as shown below:


{% highlight json %}
{
    "N100008102": [
        (170,"room.U25A")
    ],
    "N100037102": [
        (160, "room.U148") 
    ],
    "N100038102": [
        (163,"room.U141")
        (164,"room.U141")
        (165,"room.U141")
        (166,"room.U141")
    ],
    "N100040102": [
        (173, "room.U148") 
    ],
    "N100042102": [
        (170, "room.U148") 
    ],
    "N110028102": [
        (163, "room.U148") 
        (164, "room.U25A") 
    ],
...
}
{% endhighlight %}

The json object is a dictionary with keys the STADS code of the exam and
value an array with the days and rooms in which the exam has been
scheduled. Days are indicated by number corresponding to the day number
from the start of the year. For example day 01/01/2022 is day 1. This is
consistent with the imported instance.


In Python the json file can be easily obtained with the following lines of code:
```python
json.dump(dates, fp=filehandle, sort_keys=False, ignore_nan=True,
                  indent=4, separators=(',', ': '),  ensure_ascii=False)
```
where `dates` is a dictionary with exam STADS code as key and the list of days as values.


### Questions & Answers


- Should the "forbidden" and "available" information that is given
  at some of the exams be used when scheduling them?

  That would be nice, yes. They give days where the exam cannot be
  planned or the only days where it can be planned.


<!--
 <p style="color:blue">  
- Note that if you find infeasible instances it might be good
  having a look at what are the reasons for infeasibility. In MiniZinc
  it is possible to find the Miminum Unsatisfiable Subset of
  constraints that makes a problem unsatisfiable. see Chap 3.7 from
  the MiniZinc manual. Known possible infeasibility issues in E20:
  `conflicting` includes the exam itself; the exams B560001102 and
  B560003102 share a single student (5a51dabaaa908176c2b9be887a688afd)
  but are also both preassigned to start at day 4. You are welcome to
  resolve issues of this type by changing the instance data, (eg,
  removing that student or one of the exams). However, in doing this
  operation seek to apply the minimal impact on the instance.  The
  instances from E22 and E22re should not contain issues of these kind
  and are solvable.
-->

