# Introduction

This project does a thorough exploration of Primality-Testing Algorithms and also covers the design and analysis of some Greedy and Dynamic Programming algorithms.

We will assume that the reader is familiar with the basic arithmetic properties of class of integers $\mathbb{Z}$.
Some prelimnaries are covered henceforth:

## Divisibility, Primes and Composites

```{prf:definition}
If $a, b$ are integers we say that $a$ ***divides*** $b$, or that $a$ is a ***factor*** or ***divisor*** of $b$, if there exists an integer $q$ such that $b = aq$. We denote this by $a|b$. Then $b$ is a ***multiple*** of $a$. If $b > 1$ is an integer whose only factors are $\pm 1$, $\pm b$ then
$b$ is ***prime***; otherwise, $b > 1$ is ***composite***.
```

Simply put, a **Prime Number** is a positive integer $p$ having exactly two positive divisors, namely $1$ and $p$. 

For any two numbers $a$ and $b > 0$, we can always attempt to divide $a$ by $b$.

Mathematically, for any two numbers $a, b$ where $b > 0$ we have unique integers $q,r$ such that $a = qb + r$ holds where $r = 0$ or $0 < r < b$. Thus, here, $q$ and $r$ are the quotient and remainder of the division respectively. Here, if remainder is $0$ then it implies that $b$ is a factor of $a$.

The next idea that is necessary is the concept of greatest common divisor.

```{prf:definition}
Given nonzero integers $a, b$, their greatest common divisor or
GCD $d > 0$ is a positive integer that is a common divisor, that is, $d|a$ and $d|b$, and if $d_1$ is any other common divisor then $d_1|d$. We denote the greatest common divisor
of $a, b$ by either gcd$(a, b)$ or $(a, b)$.
```

The GCD is unique for any two nonzero integers (since only one common factor can be the greatest factor). Also the GCD is characterized as the least positive linear combination possible for $a, b$.

If $(a, b) = 1$ then we say that $a,b$ are **relatively prime** or intuitively, $a$ and $b$ do not share any common factors with each other.

```{prf:lemma} Euclid's lemma
Suppose $a | bc$. Then $a | b$ or $a | c$.
```

### Fundamental Theorem of Arithmetic

````{prf:theorem} 
Given any integer $n > 1$ there is a factorization
```{math}
n = p_1 p_2 \cdots p_k
```
where $p_1, \ldots , p_k$ are primes. Further, this factorization is unique up to the ordering of the factors.
````

We use the notation $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$ to denote the factorization of $n$ where $p_1, p_2, \ldots, p_k$ are the prime factors of $n$ and the exponents are greater than 0.

## Congruence and Modular Arithmetic

```{prf:definition}
Suppose $m$ is a positive integer. If $a, b$ are integers such that $m|(a−b)$ then $a$ is said to be **congruent** to $b$ **modulo** $m$ and denoted by $a \equiv b \text{ mod } m$.
```

### Euler Phi (Totient) function

```{prf:definition}
For any $n > 0$, we define $\phi(n)$ as the number of integers less than or equal to $n$ that are relatively prime to $n$.
```

````{prf:lemma}
For any prime $p$ and $m > 0$,
```{math}
\phi(p^m) = p^m − p^{m−1} 
```
````

````{prf:proof}
Proof is fairly simple.
The integers less than $p^m$ that are not relatively prime to $p^m$ are precisely the multiples of $p$.

Total number of multiples of $p$ till $p^m$
```{math}
p^m = p + (n - 1) p \implies n = p^{m - 1}
```

Hence,  $\phi(p^m) = p^m − p^{m−1}$.
````

We also note that the totient function is a multiplicative function i.e., $\phi(mn) = \phi(m)\phi(n)$ (proof has been omitted).

## Complexity Theory

````{prf:definition}
We say that $f(n) = O(n^k)$ if, for some $c$ and $n_0$, for all $n \ge n0,$
```{math}
f(n) \le c \cdot n^k
```

We say that, $f(n) = \tilde{O}(n^k)$ if, for some $c \ge 0,$
```{math}
f(n) = O(n^k\; (\log n)^c)
```

The $\tilde{O}$ notation is useful to avoid terms like $\log n$ and $\log \log n$. 

For example, it is easier to write $\tilde{O}(n)$ than the (more precise) $O(n log n log log n)$.
````