# AKS Primality Test

The AKS primality test is a deterministic primality test.
It was the foremost test that proved that the language *PRIMES* is in *P* class finally settling the issue about where *PRIMES* belongs.

## Intuition

AKS test is an extension of Fermat's Little Theorem to polynomials.

````{prf:lemma}
Let $a,n \in \mathbb{Z}$ with $(a, n) = 1$.
Then $n$ is prime iff 
```{math}
(X + a)^n \equiv X^n + a \quad (\text{mod} n)
```
````

Here, $X$ is a symbol that is part of the polynomial. 

````{prf:proof}
Using Binomial theorem,
```{math}
(X + a)^n = \sum_{k = 0}^{n} \binom{n}{k} X^{n - k} a^k
```

For $0 < k < n$,
```{math}
\binom{n}{k} = \frac{n!}{(n - k)! k!} = \frac{n \cdot (n - 1) \cdot (n - 2) \cdots (n - k + 1)}{k!}
```

Suppose $n$ is prime. Then on modulus $n$, $n | n$ in the numerator but nothing in the denominator since $k < n$ and $(k,n) = 1$ due to $n$ being prime.

Now, we are left with the $0^{th}$ and $n^{th}$ terms both having coefficients $= 1$.

For, the $0^{th}$ term, $X^n \text{ mod } n$ remains.
As for the $n^{th}$ term, $a^{n} = a \text{ mod } n$ by Fermat's Little Theorem.

To prove the other side of the biconditional, we will prove the contrapositive.

Suppose, $n$ is composite. Therefore, we assume a prime factor $p$ of $n$.
Therefore, by fundamental theorem of arithmetic, we know for some $e > 0,\quad p^e | n$ but $p^{e + 1} \nmid n$.

For the $p^{th}$ term, coefficient $= \binom{n}{p} = \frac{n \cdot (n - 1) \cdot (n - 2) \cdots (n - p + 1)}{p!}$.

$p^e$ divides only $n$ in the numerator and nothing else (since the numerator is consecutive numbers of count $p$ and only $n$ is divisible by them). But there is an additional $p$ in the denominator due to $p!$.

Which implies that, $p^{e - 1} | \binom{n}{p}$ but $p^{e} \nmid \binom{n}{p}$. Which means that $n \nmid \binom{n}{p}$ and therefore this term does not vanish.

Thus, we do not reach the $X^n + a$ form.
````

This lemma in itself gives a condition to do primality testing. But computing the coefficients of $(X + a)^n$ is exponential in the size of $n$ which makes the test extremely slow for large inputs. 

This is solved in the AKS test by evaluating the polynomials on both sides modulo another polynomial, $X^r - 1$ and checking for several different $a$'s.

So we test the congruence
```{math}
(X + a)^n \equiv X^n + a \quad (\text{mod } X^r - 1, n)
```

This will lower the degree of the polynomial and thus reduce the number of coefficients needed to be calculated to confirm the test.

```{prf:algorithm} AKS Primality Test

Input: $n \ge 2$

1. If n = $a^b$ for $a \in \mathbb{N}$ and $b > 1$, return **COMPOSITE**
2. Find the smallest $r$ such that $ord_r(n) \not \le log^2 n$
3. If $1 < (a, n) < n$ for some $a \le r$, return COMPOSITE
4. If $n \le r$, return PRIME
5. For a = 1 to $\lfloor \sqrt{\phi(r)} log n \rfloor$:
  1. If $(X + a)^n \not \equiv X^n + a \; (\text{mod } X^r − 1, n)$, return COMPOSITE.
6. Return PRIME.
```

Here, $ord_r(n)$ is the order of the element $n$ within the group $\mathbb{Z}^*_r$.
