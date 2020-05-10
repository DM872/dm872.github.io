---
layout: default
mathjax: true
title:  Sheet 2
date:   2020-04-27 09:33:19 +0100
categories: assignments
---



## Obligatory Assignment 1


<div style="float: center">
<span style="color: blue">
**Deadline: May 20, 2020, at noon**
</span>
</div>

The goal of this assignment is to implement a MILP model for the
problem of scheduling classes from courses at the faculty of Natural
Science of SDU.  A starting package containing data and code is
available from the directory `CTT` of the repository `Material` in
github.

The goals of the assignment are to:

- model the problem in MILP terms
- describe the model in a written report
- implement the model in Python
- experiment with the data made available and
- report the computational results in the report.  

The project has to be carried out individually. The deliverables, to be
collected in a tar gzip archive and submitted via SDU Assignment in
BlackBoard, are:

- the report (max 7 pages)
- the source code of the implementation.

You do not need to hand in the input data. The source code must be
organized as in the `CTT` repository made available. The report must
be placed in a directory called `doc` inside `CTT`.

<span style="color: red"> You can choose not to put your name or
identifier in any of the files submitted, if your prefer to remain
anonymous during the evaluation. BlackBoard will rename the archive
file that you submit with your exam number. Thus, you will be finally
correctly identified by the exam office. </span>

### Problem description

Given:

- A set of hourly *timeslots* (aka, time periods) $P=\\\{(h,d,w) \mid
    h\in \mbox{Hours}, d\in \mbox{Days}, w\in \mbox{Weeks}\\\}$, that
    is, 10 slots of one hour per day $\times$ 5 days $\times$ 17
    weeks). [File: `timeslots.json`.]

- A set of *events* (aka, classes) $E$. Events are derived from courses,
    weeks, sessions and sections.  Each event has a duration
    $\ell(e)$, $e \in E$ and a week where it has to take place. [File:
    `events.json`.]

- A set of *rooms* $R$. <span style="color: red">Each room has a set
  of timeslots where it is busy (Rooms
  should also have a capacity that makes them suitable or not for a
  course. This important detail will be ignored in this assignment.) [File: `rooms.json`.]</span>

- A *precedence digraph* $D=(E,A)$ where each arc $uv \in A$
    for $u,v \in E$ represents a precedence constraint that $u$ must be
    scheduled before $v$.

- Two sets of people: a set of *students* $S$, a set of
    *teachers* $T$, together with:

    - a collection of *enrollments* ${\cal Q}=\\\{E_s \subset E \mid s \in
    S\\\}$ that are events a student has subscribed to. [File: `students.json`.]

    - a collection of *teaching duties* ${\cal D}=\\\{D_t \subset E \mid t \in
  T\\\}$. [File: `teachers.json`.] 

    - teacher *unavailabilites* ${\cal U}=\\\{U_t \subset P \mid t \in  T\\\}$


<!--
- *Preassignments*: schedule of mandatory courses $M=\{(e,r,p) \mid e \in E, r\in R,
    p\in P\}$
-->


Task:

A *timetable* is a schedule of events in timeslots and rooms
throughout the semester.

<span style="color: red">A *conflict* arises if a resource (room,
teacher, student, course) is used by more than one event at a
time.</span>

A timetable is feasible if it satisfies all (hard) constraints given
below.

The task of the assignment is to find a timetable that is feasible and
good with respect to the desirability criteria given below.




Constraints (hard constraints):

- all events are scheduled
- there are no room conflicts
- there are no teacher conflicts
- <span style="color: red">there are no course conflicts and there is at most one event per day per course</span>
- the precendences within the weeks are met
- forbidden slots are not used
- paired courses are sychronized 


Desirability criteria (soft constraints):

- student conflicts are minimized 
- weekly stability is promoted
- the number of events per day per teacher is minimized 
- <span style="color: red">bad slots are avoided in a way proportional to their degree of discomfort (in the figure below, darker shades of green indicate higher undesirability/discomfort).</span>


![trends]({{ "/assets/bad_slots.jpg" | absolute_url }}){:width="60%" .center-image}

