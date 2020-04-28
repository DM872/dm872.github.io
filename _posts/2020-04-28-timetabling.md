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
available from the directory `CTT` of the repository Material in
github.



Given:

- A set of time periods (aka, *timeslots*) $P=\{(h,d,w) \mid
    h\in \mbox{Hours}, d\in \mbox{Days}, w\in \mbox{Weeks}\}$, that is,
    10 slots of one hour per day $\times$ 5 days $\times$
    17 weeks).


- A set of **rooms** $R$ (in fact just two: seminar room + dummy)

- A set of **events** or classes $E$ (mandatory and
    elective). Events are derived from courses, weeks, sessions and
    sections.
    Each event has a duration $\ell(e)$, $e \in E$

- A **precedence digraph** $D=(E,A)$ where each arc $uv \in A$
    for $u,v \in E$ represents a precedence constraint that $u$ must be
    scheduled before $v$.

- Two sets of people: a set of **students** $S$, a set of
    **teachers** $T$, together with:

    - a collection of **enrollments** ${\cal Q}=\{E_s \subset E \mid s \in
    S\}$ that are events a student has subscribed to (**post
      enrollment model})

    - a collection of **teaching duties** ${\cal D}=\{D_t \subset E \mid t \in
  T\}$

    - teacher **unavailabilites** ${\cal U}=\{U_t \subset P \mid t \in  T\}$


- **Preassignments**: schedule of mandatory courses $M=\{(e,r,p) \mid e \in E, r\in R,
    p\in P\}$


Task:

Schedule events in timeslots and rooms throughout the semester such
  that the timetable is feasible and appealing from different
  **perspectives** (resources).


**Constraints** (hard constraints)

- Enforce all events scheduled
- Prevent room conflicts
- Prevent staff conflicts
- Enforce fixed preassignments
- Enforce fixed rooms
- Enforce max one event x day x crs
- Enforce precedences
- Enforce banned slots
- Enforce pairings


**Objective(s)** (soft constraints):


- Weekly stability %(p_slv, p_dat, 20.0);
- Usage of seminarrum %(p_slv, p_dat, 1.0);
- Student/Instructor conflicts %(p_slv, p_dat, 15.0);
- Events x day x teacher %(p_slv, p_dat, 3.0);
- Instructor Conflicts %(p_slv, p_dat, 30.0);
- Bad slots (see Figure~\ref{badslots}) %(p_slv, p_dat, 1.0, bs);

