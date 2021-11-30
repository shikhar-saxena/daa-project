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


<!-- 
While the lemma constitutes a primality test in itself, verifying it takes
exponential time: the brute force approach would require the expansion
of the (x + a)n polynomial and a reduction modn of the resulting n + 1
coefficients.
The congruence is an equality in the polynomial ring Zn[x]. Evaluating
in a quotient ring of Zn[x] creates an upper bound for the degree of the
polynomials involved. The AKS evaluates the equality in Zn[x]/ (xr − 1) ,
making the computational complexity dependent on the size of r. For clarity,
this is expressed as the congruence
(x + a)n ≡ xn + a
(mod xr − 1, n)
Note that all primes satisfy this relation. This congruence can be checked
in polynomial time when r is polynomial to the digits of n.
The AKS algorithm evaluates this congruence for a large set of a values,
whose size is polynomial to the digits of n. The proof of validity of the AKS
algorithm shows that one can find an r and a set of a values with the above
properties such that if the congruences hold then n is a power of a prime.
The algorithm can be written as follows:
Input:
Integer n > 1.
Output:
1. If n = ab for a ∈ N and b > 1, return composite.
2. Find the smallest r such that ordr(n) > (log2 n)2.
3. If 1 < (a, n) < n for some a ≤ r, return composite.
4. If n ≤ r, return prime.
5. For a = 1 to ⌊
√
ϕ(r) log2 n⌋ do
if (x + a)n ̸= xn + a (mod xr − 1, n), return composite;
6. Return prime.
Complexity:
In the first version of the paper, the authors proved the asymptotic time
complexity of the algorithm to be ˜O
(
log12 n
)
. However, this upper bound
was rather loose; a widely-held conjecture about the distribution of the
Sophie Germain primes would, if true, immediately cut the worst case down
to ˜O
(
log6 n
)
.
While the algorithm is of immense theoretical importance, it is not used
in practice, for it is more complex, time-consuming and space-consuming
than other algorithms like Miller–Rabin primality test.
METHODS OF PRIMALITY TESTING
7

 If (a, n) = 1, then the order of a modulo n is the least power m
such that am ≡ 1 mod n. We will write order(a) or |⟨a⟩| or |a| for the order of a.
Equivalently, the order of a is the order of a considered as an element of the unit
group U(Zn).
Since the order of U(Zn) equals φ(n), we immediately get that the order of any
element modulo n must divide φ(n). -->

<!-- π(x)
x
∼
1
ln x as x → ∞,
where π(x) represents the number of primes less than the positive real number x. -->