## Sheet 4


### Task 1

Give an extensive formulation of the multicommodity flow problem and
show that it can be derived by Dantzig Wolfe decomposition of the
previously seen (compact) arc flow formulation. 

- What is the complete Master Problem?
- What is the column generation subproblem?



### Task 2

Consider generalized assignment problem with equality constraints:

$$
\begin{align}
\max &\sum_{i=1}^m\sum_{j=1}^n c_{ij}x_{ij}\\
&\sum_{j=1}^n x_{ij}= 1 \qquad  i = 1,\ldots, m\\
&\sum_{i=1}^m a_{ij} x_{ij}\leq  b_j \qquad  j = 1,\ldots,n\\
&x \in \{0, 1\}^{mn}.
\end{align}
$$

Solve an instance by delayed column generation treating the constraints $\sum_{j=1}^n x_{ij}= 1 \qquad  i = 1,\ldots, m$ as the complicating ones
and 
$m=3,n=2,[a_{ij}]=\begin{bmatrix}5&3\\\\3&8\\\\2&10\end{bmatrix},[c_{ij}]=\begin{bmatrix}20&16\\\\15&19\\\\19&14\end{bmatrix}$
and $[b_j]=\begin{bmatrix}6\\\\21\end{bmatrix}$.

{% if page.solution %}
<font color="blue">
Solution:


This is an example of unrelated parallel machine scheduling problem, where machines are indexed by $j$ and jobs (activities, tasks) by $i$.

We can apply Dantzig-Wolfe decomposition to GAP treating the assignment constraints as the linking and complicating constraints defining the master problem and the machine capacity constraints as the block constraints defining the subproblems.

Let $K_j$ be the number of solutions to the knapsack subproblem:
$$
\sum_{1\leq i\leq m}w_{ij}y^j_i\leq d_j\\
y^j_i\in \{0,1\}, \quad  i=1,\ldots,m
$$
Any solution to this problem, indexed by $k=1,\ldots,K_j$, i.e. $\vec y^j_k=(y^j_{1k},y^j_{2k},\ldots,y^j_{mk})$, represents a feasible assignment of tasks to a machine $j$.

The master problem becomes:  
$$
\begin{align}
\max &\sum_{1\leq j\leq n}\sum_{1\leq  k\leq K_j}\left(\sum_{1\leqi\leq m} p_{ij}y^j_{ik}\right)\lambda_k^j}\\
&\sum_{1\leq j\leq n}\sum_{1\leq  k\leq K_j}y^j_{ik}\lambda_k^j=1,\qquad i=1,\ldots,m\\
&\sum_{1\leq  k\leq K_j}\lambda_k^j=1,\qquad j=1,\ldots,n\\
&\lambda_k^j\in \{0,1\}, \qquad j=1,\ldots,nk=1,\ldots,k
\end{aling}
$$
To solve the problem by branch and bound we need to find the solutions of the linear relaxation. Let LMP be the linear relaxation of the problem. 
Since we have exponentially many variables, we solve the problem by (delayed) column generation. Let RLMP be the problem restricted to a subset of variables.
The pricing of a variable (reduced cost) is given by:
$$

$$ 



</font>
{% endif %}



### Task 3


You are the person in charge of packing in a large company. Your job
is to skillfully pack items of various weights in a box with a
predetermined capacity; your aim is to use as few boxes as
possible. Each of the items has a known weight and the upper limit of
the contents that can be packed in a box is 9 kg. There is no concern
with the volume they occupy. So, how should these items be packed?

|Weights of items to be packed in bins of size 9|
|-----------------------------------------------------------------------|
|6, 6, 5, 5, 5, 4, 4, 4, 4, 2, 2, 2, 2, 3, 3, 7, 7, 5, 5, 8, 8, 4, 4, 5|
|-----------------------------------------------------------------------|




![instance]({{ "/assets/images/bpp-instance.png" | absolute_url }}){:width="50%" .center-image}


This is an example of a problem called the *bin packing problem*. It can
be described mathematically as follows.

Bin packing problem

There are $n$ items to be packed and an infinite number of available bins
of size $B$. The sizes $0\leq s_i \leq B$ of individual items are assumed to be
known. The problem is to determine how to pack these $n$ items in bins of
size $B$ so that the number of required bins is minimum.

1. Formulate the problem using a compact formulation and an extensive
formulation. 

2. Solve the given example using the extensive formulation. Solve the linear relaxation of the master problem by column generation and draw a plot about the dual bound development during the process. 

3. Continue the process with branch and price if the solution found at the previous point is not integral.




```python

def BinPackingExample():
    B = 9
    s = [6, 6, 5, 5, 5, 4, 4, 4, 4, 2, 2, 2, 2, 3, 3, 7, 7, 5, 5, 8, 8, 4, 4, 5]
    return s,B


def FFD(s, B):
    remain = [B]
    sol = [[]]
    for item in sorted(s, reverse=True):
        for j,free in enumerate(remain):
            if free >= item:
                remain[j] -= item
                sol[j].append(item)
                break
        else:
            sol.append([item])
            remain.append(B-item)
    return sol

```

You find these data and some starting templates for your implementations
in Python in our git repository [GIT]:

- A template for the compact formulation: `compact_template.py`.

- A template for the extended formulation with delayed column generation: `extensive_template.py`



To add columns to your model without resolving from
scratch see:

- In `gurobipy`, the last example from this doumentation page:
  [Modify a model (gurobi.com)](https://www.gurobi.com/documentation/10.0/examples/modify_a_model.html)

- In Python MIP see documentation for `Column` and `add_var`.

- In Pyomo see
  [cutting_stock.py](https://github.com/Pyomo/pyomo/blob/main/examples/pyomo/columngeneration/cutting_stock.py)

- In Pyscipopt there is a different philosophy. See
  [test_pricer.py](https://github.com/Pyomo/pyomo/blob/main/examples/pyomo/columngeneration/cutting_stock.py). Alternatively
  it is possible to follow this [example](../assets/cutstock.py).