---
layout: default
mathjax: true
title:  Data fitting
date:   2021-05-13 09:33:19 +0100
categories: exercises
---

## Data Fitting

In this exercise we study the application of linear programming to an
area of statistics, namely, regression. You will have use the material
developed in this task to fit the data of the development of
Coronavirus in Denmark or other countries of your choice.

Data resources:

- [Denmark](https://www.sst.dk/da/corona/tal-og-overvaagning)

- [Italy](https://github.com/pcm-dpc/COVID-19)

- [Kaggle Competition](https://www.kaggle.com/covid19) 


Consider a set of $m$ measurements. A way to summarize these data is by their mean
$$
\bar{x}=\frac{1}{m} \sum_{i=1}^mx_i
$$
An alternative way is by the median, ie, the measurement that is worse
than half of the other scores and better than the other half.

There is a close connection between these statistics and
optimization. It is easy to show that the mean is the measure that
minimizes the sum of squared deviation between the data points and
itself and that the median minimizes the sum of the absolute values of
the differences between each data point and itself. (How?)


Consider now a set of points on a two-dimensional space
$S=(x_1,y_1),\ldots,(x_m,y_m)$. The points are measurements of a response
variable given some control variable, for example, blood pressure given
the weight of a person. The points hint at a linear dependency between
the variables representing the two dimensions. We may assume a random
fluctuation around the right value and hence the following regression
model:
\\[
y=ax+b+\epsilon
\\]
Specifically, for our set of points $S$ we have
\\[
y_i=ax_i+b+\epsilon_i, \quad i=1,\ldots,m
\\]

We thus want to find a line that best fits the measured points. That is,
we wish to determine the (unknown) numbers $a$ and $b$. There is no
unique criterion to formulate the desire that a given line ''best fits''
the points. The task can be achieved by minimizing, in some sense, the
vector $\epsilon$. As for the mean and median, we can consider
minimizing either the sum of the squares of the $\epsilon_i$'s or the
sum of the absolute values of the $\epsilon_i$'s. These concepts are
formalized in measure theory by the so called $L^p$-norm ($1\leq p <
\infty$). For the vector $\epsilon$:

\\[
\parallel \epsilon \parallel_p=\left(\sum_i
  \epsilon_i^p\right)^{1/p}
\\]

The method of least squares, which is perhaps the most popular,
corresponds to $L^2$-norm. The minimization of $L^2$-norm for the vector
$\epsilon$ in the variables $a$ and $b$ has a closed form solution that
you may have encountered in the statistics courses.  This method needs
not always to be the most suitable, however. For instance, if a few
exceptional points are measured with very large error, they can
influence the resulting line a great deal. Just as the median gives a
more robust estimate of a collection of numbers than the means, the
$L^1$ norm is less sensitive to outliers than least square regression
is. The problem is to solve the following minimization problem:

\\[
\mathrm{argmin}_{a,b} \sum_i |\epsilon_i|= \mathrm{argmin}_{a,b} \sum_i |ax_i+b-y_i|
\\]

Unlike for least square regression, there is no explicit formula for
the solution of the $L^1$-regression problem. However the problem can be
formulated as a linear programming problem. Show how this can be done.


#### Fitting an exponential function with least squares and linear programming


We saw above that fitting a linear model leads to a least squares or a
linear programming optimization problem. However, by transforming the $x$-axis and/or the $y$-axis with the logarithm we can fit also polynomial functions and exponential functions. 


![trends]({{ "/assets/trends.png" | absolute_url }}){:height="60%" width="56%" .center-image}


<!-- 
{: .center-image }
{:class="img-responsive"}
-->

For example, we can transform the non-linear models of the type, e.g.,
$exp(x) = a \cdot bx$ or $poly(x) = a \cdot x b$ into linear models
after the transformation of the $x$ and $y$ axis.  Show how this can
be done.

<!--
by
taking the log of the running times and the log of the models. For
example, $\log(poly(x)) = \log(a · bx ) = \log(b) · x + \log(a) = a' · x +
b' = lin'(x)$, where we have introduced the transformations $a' =
log(b)$ and $b' = log(a)$. Then, by introducing $y'[i] = log(y[i])$, we can
fit the model $lin'(x) = a' · x + b'$ to $y'$.
-->


#### Your subtask

Using the data from the data sources listed above about the
developement of the coronavirus infection, assess whether the growth
is exponential or whether it was at any time exponential.




#### Estimation of Infectious Disease Models

A different approach to modelling outbreak of an infectious disease is
through simulation.  We derive a basic model to describe the spread of
infection in the population. We use a standard discrete time
compartment model to represent the system. Individuals are separated
into three compartments based on their status with respect to the
disease: susceptible (S), infected (I), or recovered (R). We assume
that once an individual has contracted the disease and recovered, they
are immune from that point forward (i.e., they do not return to the
susceptible pool). The discrete time model representing this systems
is given by:

$$
\begin{array}{l}
I_i =  \frac{\beta I^\alpha_{i-1}S_{i-1}}{N}\\
S_i=S_{i-1}-I_i
\end{array}
$$


These two difference equations describe the propagation of the disease
in the population. As a generation-based model, it is assumed that all
the individuals infected at time $i$ have recovered by time $i +
1$. $I_i$ and $S_i$ are the number of infected and susceptible
individuals at time $i$, respectively. The population size is given by
$N$, and $\alpha$ and $\beta$ are model parameters.


We can use least-squares to estimate the parameters $\beta$ and
$\alpha$ from real-life data. Let $D$ be the set of indices for the
serial intervals, for example days. The reported cases (known input)
are given by $C_i$, and the variable $\epsilon_i^I$ is the residual
between the measured and calculated cases. The full problem
formulation is given by,

$$
\begin{array}{llllll}
\min &\sum_{I\in SI}(\epsilon_i^I)^2\\
&I_i=\frac{\beta I^{\alpha}_{i-1}S_{i-1}}{N} & & \forall i \in D\setminus\{1\}\\
&S_i=S_{i-1}-I_i &&\forall i \in D\setminus \{1\}\\
&C_i = I_i + \epsilon_i^I\\
&0 \leq I_i, S_i \leq N\\
&0.5\leq\beta \leq 70\\
&0.5\leq \alpha \leq 1.5
\end{array}
$$


#### Your subtask

Specify what type of optimization problem is this and find out whether you can solve it with Gurobi.

The case is taken from sec 7.4.3 of the book:

> Bynum, M.L., Hackebeil, G.A., Hart, W.E., Laird, C.D., Nicholson, B., Siirola, J.D., Watson, J.-P., Woodruff, D.L.. [Pyomo – Optimization Modeling in Python. Third Edition.](http://www.springer.com/mathematics/book/978-3-319-58819-3)  Springer, 2021.

Data and implementation code are available [here](https://github.com/Pyomo/pyomo/tree/main/examples/pyomobook/nonlinear-ch/disease_est). Try to run the code which require [pyomo](http://www.pyomo.org/) and [Ipopt](http://www.pyomo.org/) and interpret the output. 



<!--
The solution of nonlinear programming problems presents several
challenges that do not exist for linear problems. For example, most
modern, efficient NLP solvers require derivatives of the constraints
and the objective function. Since the functions are nonlinear, this
requires accurate numerical evaluation of these derivatives at a given
trial point. Additionally, in the case of non-convex problems,
multiple local minima may exist (due to the shape of the objective
function or the constraints), and specifying a suitable starting point
may be critical.

Pyomo supports the following general nonlinear programming formulation:

$$
\begin{array}{lllllll}
\min& f(x)\\
s.t.& c(x) = 0\\
&d^L \leq d(x) \leq d^U\\
&x^L \leq x \leq x^U
\end{array}
$$

We assume that the functions $f,c,d$ are continuous and smooth, with
continuous first (and possibly second) derivatives.

#### Your subtask

Implement and solve the model above in Pyomo.
-->


