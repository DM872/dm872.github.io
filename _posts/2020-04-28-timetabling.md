---
layout: default
mathjax: true
title:  Sheet 2
date:   2020-04-27 09:33:19 +0100
categories: assignments
---



## Obligatory Assignment 1


The goal of this assignment is to implement a MILP model for the
problem of scheduling classes from courses at the faculty of Natural
Science of SDU.  A starting package containing data and code is
available from the directory `CTT` of the repository `Material` in
github.

The goals of the assignment are:

- model the problem in MILP terms
- describe the model in a written report
- implement the model in Python
- experiment with the data made available and
- report the computational results in the report.  

The project has to be carried out individually. The deliverables to be
collected in a tar gzip archive and submitted via SDU Assignment in
BlackBoard, are:

- the report (max 7 pages)
- the source code of the implementation.

You do not need to hand in the input data. The source code must be
organized as in the `CTT` repository made available. The report must
be placed in a directory called `doc` inside `CTT`.



### Problem description

Given:

- A set of hourly time periods (aka, *timeslots*) $P=\\\{(h,d,w) \mid h\in
    \mbox{Hours}, d\in \mbox{Days}, w\in \mbox{Weeks}\\\}$, that is, 10
    slots of one hour per day $\times$ 5 days $\times$ 17 weeks).

- A set of *events* or classes $E$. Events are derived from courses,
    weeks, sessions and sections.  Each event has a duration
    $\ell(e)$, $e \in E$ and a week where it has to take place.  File
    `event_list`.

- A set of *rooms* $R$ 

- A *precedence digraph* $D=(E,A)$ where each arc $uv \in A$
    for $u,v \in E$ represents a precedence constraint that $u$ must be
    scheduled before $v$.

- Two sets of people: a set of *students* $S$, a set of
    *teachers* $T$, together with:

    - a collection of *enrollments* ${\cal Q}=\\\{E_s \subset E \mid s \in
    S\\\}$ that are events a student has subscribed to 

    - a collection of *teaching duties* ${\cal D}=\\\{D_t \subset E \mid t \in
  T\\\}$

    - teacher *unavailabilites* ${\cal U}=\\\{U_t \subset P \mid t \in  T\\\}$


<!--
- *Preassignments*: schedule of mandatory courses $M=\{(e,r,p) \mid e \in E, r\in R,
    p\in P\}$
-->


Task:

A timetable is a schedule of events in timeslots and rooms throughout the semester.
A timetable is feasible if it satisfies all (hard) constraints given below.

The task of the assignment is to find a timetable that is feasible and
good with respect to the criteria given below.


Constraints (hard constraints):

- Enforce all events scheduled
- Prevent room conflicts
- Prevent staff conflicts
- Enforce max one event x day x crs
- Enforce precedences
- Enforce banned slots
- Enforce pairings


Desirability criteria (soft constraints):

- Student conflicts
- Weekly stability 
- Events x day x teacher 
- Bad slots: in the figure below, darker shades of green indicate higher undesirability.


![trends]({{ "/assets/bad_slots.jpg" | absolute_url }}){:width="60%" .center-image}

