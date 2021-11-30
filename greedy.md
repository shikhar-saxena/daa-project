# Greedy Algorithm for Egyptian Fractions

In mathematics, the **greedy algorithm for Egyptian fractions** is a greedy algorithm, first described by Fibonacci, for transforming rational numbers into Egyptian fractions.

```{prf:definition}
An Egyptian fraction is a representation of an irreducible fraction as a sum of distinct unit fractions, such as

$5/6 = 1/2 + 1/3$.

Unit fractions are fractions with numerator $= 1$.
```

As the name indicates, these representations have been used as long ago as ancient Egypt, but the first published systematic method for constructing such expansions is described in the *Liber Abaci* by Fibonacci. It is called a greedy algorithm because at each step the algorithm chooses greedily the largest possible unit fraction that can be used in any representation of the remaining fraction.

## Greedy Choice

For the fraction $x/y$ we take out $\frac{1}{\lceil \frac{y}{x}\rceil}$ which is the maximum possible unit fraction that can be taken out from $x/y$.

Hence, we are greedy in our choice of picking the unit fraction.

Now, for the remaining fraction, repeat the same stuff until we reach a fraction which is a unit fraction in which.

As each expansion step reduces the numerator of the remaining fraction to be expanded, this method always terminates with a finite expansion. However, compared to ancient Egyptian expansions or to more modern methods, this method may produce expansions that are quite long, with large denominators.

# The MST Problem

*Input:* An undirected graph G = (V,E); edge weights $w_e$.

*Output:* A tree T = (V, E') with $E'\subseteq E$, that minimizes weight(T) = $\sum_{e\in E'} w_e$

# Greedy Approach: Kruskal's Algorithm

**Greedy approach (here):** We will add minimum weight edges that do not produce a cycle in the graph.

* Start with an empty graph.
* Repeatedly add next edge (with least weight) that doesn't produce a cycle.
* After some point we will reach the MST.

## Why is it Greedy?

Because we are greedy in our choice of edges (to get the MST) and also we choose one local optimum to another so as to get a global optimum.

## Proof of correctness

### The CUT Property

**CUT Property:** Suppose edges X are part of a MST of $G = (V,E)$. Pick any subset of nodes S for which X does not cross between $S$ and $V-S$, and let e be the lightest edge across this partition. Then $X \cup \{e\}$ is part of some MST.

Essentially the cut property says that if we have some edges in our MST, then we can still increase the edge set and still be part of an MST.

````{prf:proof}
- Edges X are part of some MST T
- Assume new edge e is not in T
- Construct a different MST T' containing $X \cup \{e\}$
- Add edge e to T, and this creates a cycle having another edge e' between S and V-S. *If we remove edge e', we are left with $T' = T \cup \{e\} - \{e'\}$* which we will show to be a tree. e and e' should be of same weight (because we picked lightest edge and T is also an MST).
- T' is connected since e' is a cycle edge (removing the cycle edge cannot disconnect the graph). 
- And T' has the same number of edges as T, so it is also a tree (since both will have |V|-1 edges).

Any connected, undirected graph $G=(V,E)$ with $|E| = |V| - 1$ is a tree.
(A tree on n nodes has $n-1$ edges).

Moreover, T' is a MST, Compare its weight to that of T: weight($T'$) = weight$(T) + w(e) - w(e')$.

$\therefore$ Kruskal's algorithm is correct (since it satisfies the cut property).

````

## Kruskal's algorithm implementation

### Disjoint-set data structure

This data structure stores a collection of disjoint sets. Each tree in a forest is its own set with the root node being the representative of the set. We will use it here to get the MST.

```
procedure kruskal(G, w)
Input: A connected undirected graph G with edge weights w_e
Output: A MST defined by edges X

for all u in V:
    makeset(u) // makeset(x) creates a singleton set containing just x

X = {}
Sort the edges E by weight
for all edges {u,v} in E, in increasing order of weight:
    if find(u) != find(v): // find(x): to which set does x belong
        add edge {u,v} to X
        union(u,v)
```

```
procedure makeset(x)
pi(x) = x // parent pointer
rank(x) = 0 // Rank is the height of the sub tree hanging from that node
```

Function find returns the root node of the node x.

```
function find(x)
while x != pi(x): x = pi(x)
return x
```

```
procedure union(x,y)
rx = find(x)
ry = find(y)
if rx == ry: return
if rank(rx) > rank(ry): pi(ry) = rx
else: 
    pi(rx) = ry
    if rank(rx) == rank(ry): rank(ry) = rank(ry) + 1
```

union will give us the merge of the two sets.

#### Three Properties of Rank(x)

- For any x, rank(x) < rank(pi(x)).
- Any root node of rank k has atleast $2^k$ nodes in its tree. (we can prove this using induction).
- If there are n elements overall, there can be atmost $n/2^k$ nodes of rank k.

### Analysis

- Makeset taken O(1) time
- Find takes O(log n) time
- Union takes O(log n) time

Therefore, overall it takes $O((|E| + |V|) \log |V|)$ time.
