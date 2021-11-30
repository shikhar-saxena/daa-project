# Fermat's Test

Fermat's Little Theorem allows us to prove that a number is composite without actually factoring it.

````{prf:theorem} Fermat's Little Theorem
If $p$ is prime and $(p, a) = 1$ then

```{math}
a^{p - 1} \equiv 1 \text{ mod } p
```
````

````{prf:proof}
We assume $i \in {1,2,..., p - 1}$.

The numbers $a\cdot i$ mod $p$ are distinct because if $a\cdot i \equiv a\cdot j$ (mod $p$) then dividing both sides by $a$ gives $i \equiv j$ (mod $p$). They are nonzero because $a\cdot i \equiv 0$ similarly implies $i \equiv 0$. (and we can divide by $a$ so we assume $a$ is nonzero and therefore relatively prime to $p$).

Thus, both the sets $\{1,2,\ldots, p - 1\}$ and $\{a \cdot 1$ mod $p, a \cdot 2$ mod $p,\ldots, a \cdot (p - 1)$ mod $p\}$ are equal.

If we multiply together the elements in each of these representations we get 
```{math}
(p - 1)! \equiv a^{p - 1} \cdot (p - 1)! (\text{mod } p)
```
Dividing each side by $(p - 1)!$ we get the proof to our theorem.
````

```{prf:remark}
An important thing to note is that the *inverse* of Fermat's Little Theorem is not always true i.e., if $a^{n−1} \equiv 1 (\text{mod } n)$ for some $a$ with $a \not \equiv 0 (\text{mod } n)$, then $n$ might not be prime.

Such numbers are known as ***Fermat pseudoprimes***.
```

````{prf:example}
```{math}
2^{340} \equiv 1 (mod 341)
```
but $341 = 11\cdot 31$ which is composite.

We say that $341$ is a Fermat pseudoprime (to the base $2$).
````

Another thing to note is that it is even possible for $a^{n−1} \equiv 1$ (mod $n$) to hold for every $a$ with $(a,n) = 1$, where $n$ is composite. This occurs if $n$ is a **Carmichael number** (also called an absolute *Fermat pseudoprime*).

Carmichael numbers are fairly rare but some examples are $561, 1105, 1729,$ and so on.
For a randomly chosen odd integer n with 100 to 300 digits, the probability that $n$ is a Carmichael number appears to be exceedingly
low. 

If $n$ is composite and not a Carmichael number, then there are at most $\phi(n)/2$ values of $a$ ($1 \le a \le n$) for which Fermat's little Theorem holds. Which means that the probability of error for any test case $a$ is atmost half. 

The Fermat's Test is summarized as follows:
```{prf:algorithm}
**Input:** n > 1

1. for $i = 1$ to $k$ do
	1. choose random $a \ni 2 \le a \le n − 1$.
	2. if $a^{n} \not \equiv a$ (mod $n)$, return COMPOSITE.
2. return PROBABLY PRIME.
```

With fast powering algorithm, each computation of $a^n$ takes $\tilde{O}(n^2)$ time, making the overall complexity of the Fermat Test $\tilde{O}(k n^2)$, where $k$ is the number of times we run the test.

<!-- # Pocklington-Lehmer Primality Test

````{prf:theorem}
Suppose $n − 1 = f r$ with $(f, r) = 1$ and suppose that a complete factorization of $f$ is known. 

Suppose that there exists an $a$ such that 

```{math}
a^{n−1} \equiv 1 \text{ mod } n \text{ and } \left(a^{\frac{n−1}{q}, n \right) = 1
```

for every prime factor $q$ of $f$. Then every prime factor of $n$ is congruent to $1$ mod $f$.
```` -->

# Solovoy Strassen Test

````{prf:definition} Jacobi Symbol
If $n$ is a positive odd integer with prime factorization $n = p_1^{e_1} \cdots p_k^{e_k}$ and a is a positive integer then the Jacobi symbol is defined as
```{math}
(a/n) = (a/p_1)^e_1 \cdots (a/p_k)^e_k.
```
````

Some properties of Jacobi Symbol are as follows:

If $m, n$ are odd positive integers, then
1. $(2/n) = (−1)^{\frac{n^2 - 1}{8}}$
2. $(m/n) = (−1)^{\frac(m−1)(n−1)}{4}(n/m)$.

````{prf:definition} Euler pseudoprime
An *odd composite integer* $n$ is an Euler pseudoprime to the base b if
```{math}
b^{\frac{n - 1}{2}} \equiv (b/n) mod n,
```
where (b/n) is the *Jacobi symbol*.
````

````{prf:theorem} Solvay-Strassen Theorem
If n is an odd composite integer, then n is an Euler pseudoprime for at most one-half of the bases b with $1 < b < n$ and $(b, n) = 1$
````

The test is as follows:

```{prf:algorithm} Solovay–Strassen primality test

**Input:** An odd integer n

1. Choose k random integers $b_1,\cdots , b_k$ with $1 < b_i < n$
2. For $i = 1,\cdots , k$
	1. Compute $(b_i, n)$ (by the Euclidean algorithm). If $(b_i, n) > 1$, then return COMPOSITE
	2. Compute $b_i^{(n−1)/2}$ mod $n$ and $(b_i/n)$ mod $n$. If these two are not equal then return COMPOSITE
3. return PROBABLY PRIME
```

Here, the probability that $n$ is actually prime is greater than $1 - 2^{-k}$.