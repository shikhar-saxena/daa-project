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

The numbers $a\cdot i$ mod $p$ are distinct because if $a\cdot i \equiv a\cdot j$ (mod $p$) then dividing both sides by $a$ gives $i \equi j (mod p)$. They are nonzero because $a\cdot i \equiv 0$ similarly implies $i \equiv 0$. (and we can divide by $a$ so we assume $a$ is nonzero and therefore relatively prime to $p$).

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
		2. if $a^{n} \not \equiv a (mod n)$, return COMPOSITE.
4: return PROBABLY PRIME.
```

We can improve upon the limitations of Fermat's test by further restricting the test-condition.

# The Euler Test

If $n$ is an odd prime, we know that an integer can have at most two square roots, mod n. In particular, the only square roots of 1 (mod n)
are ±1.
If a ≡/ 0 (mod n), a(n−1)/2 is a square root of a(n−1) ≡ 1 (mod n), so
a(n−1)/2 ≡ ±1 (mod n).
If a(n−1)/2 ≡/ ±1 (mod n) for some a with a ≡/ 0 (mod n), then n is
composite.
Euler Test: For a randomly chosen a with a ≡/ 0 (mod n), compute
a(n−1)/2 (mod n).
i) If a(n−1)/2 ≡ ±1 (mod n), declare n a probable prime, and
optionally repeat the test a few more times.
If n is large and chosen at random, the probability that n is
prime is very close to 1.
ii) If a(n−1)/2 ≡/ ±1 (mod n), declare n composite.
This is always correct.
The Euler test is more powerful than the Fermat test.
If the Fermat test finds that n is composite, so does the Euler test.
But the Euler test may find n composite even when the Fermat test
fails. Why?
If n is an odd composite integer (other than a prime power),
1 has at least 4 square roots mod n.
So we can have a(n−1)/2 ≡ β (mod n), where β ≠ ±1 is a square
root of 1. Then an−1 ≡ 1 (mod n). In this situation, the Fermat
Test (incorrectly) declares n a probable prime, but the Euler
test (correctly) declares n composite
