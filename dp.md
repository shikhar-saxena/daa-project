# Longest path in DAGs

Longest path in a general graph is NP-complete. Problem of Hamiltonian path is NP-complete (Hamiltonian paths are the longest path). However, in DAGs finding longest part can be solved using Dynamic Programming.

Dynamic Programming is just a DAG of sub-problems. Once we find the order in which subproblems are solved (and how they depend on each other) we can use recursion in that order and employ dynamic programming. We can construct the DAG for our problem and topologically sort it.

## Solution

We can modify the algorithm for shortest path in DAGs stated above to find the solution for this problem. The solution will be correlated to the longest subsequence problem stated later and hence the algorithm for that question will serve as a dynamic programming solution for this question as well.

### Why doesn't longest path in DAG solution for Hamiltonian paths?

If there are cycles in a path, then there will be deadlocks (during recursion). In a general graph there can be cycles and back edges. In such a case Dynamic Programming will not work. That's why this problem is tougher.

## Longest increasing subsequence (LIS)

(Input): Sequence of numbers $a_1, \cdots , a_n$
A subsequence is $a_{i_1},a_{i_2},\cdots, a_{i_k}$ where $1 \le i_1 < i_2 < \cdots i_k \le n$.

An increasing subsequence is one in which numbers are getting strictly larger.

**The task is to find the increasing subsequence of greatest length.**

### Example
The sequence is 5, 2, 8, 6, 3, 6, 9, 7.

Subsequences can be 5, 2, 8, 7; etc.

Increasing subsequences are 5, 8, 9; 2, 6, 7; and the longest one is 2, 3, 6, 9.

### Underlying DAG here
Establish a node i for each element $a_i$ and add directed edges $(i, j)$ whenever it is possible for $a_i$ and $a_j$ to be consecutive elements in an increasing subsequence i.e., whenever $i < j$ and $a_i < a_j$.

Notice that all edges will be from left to right by our definition. So this DAG is already topologically sorted. Here, the longest subsequence is nothing but the longest path in the DAG. But here, the longest path may not start from the first node.

### Our DAG of Sub-Problems
We define $L(j)$ is the length of the longest path-the longest increasing subsequence-ending at $j$. We know these problems are overlapping.

collection of subproblems $\{L(j): 1 \le j \le n\}$

So, we can define our subproblems as follows:

$$L(j) = 1 + max\{L(i): (i,j) \in E\}$$

This recursion will not get into deadlock. So we can employ this dynamic programming to compute the longest path.

***Dynamic Programming: There is an ordering on the subproblems, and a relation that shows how to solve a subproblem given the answers to smaller subproblems, that is, subproblems that appear earlier in the ordering***

Here, each $L_i$ can be stored into an array for constant lookup for further cases. This is also known as table of answers to the subproblems. Here, it is a 1-D array. But in tougher problems there can be more parameters involved which can lead to higher dimension arrays.

Here, base case L(1) = 1 (since we will count the first element).

### Algorithm
````{prf:algorithm}
1. for $j = 1, 2,\ldots, n$:
	1. $L(j) = 1 + max\{L(i): (i,j) \in E\}$
2. return $max_j \; L(j)$
````