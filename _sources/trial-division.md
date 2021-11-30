# Trial Division Test

**Trial Division** is the most laborious yet easiest to understand of the integer factorization algorithms.

## Method

Given an integer $n$, the trial division consists of sequentially testing whether $n$ is divisible by any smaller number. So for a small number, we can use the same approach to factor the number as well.

The choice of trial divisors is not fixed. A loose upper bound is to check till $n - 1$ or we can bring it down to $n/2$ since if $n$ is composite then $n = ab$ where if $a > n/2$ then we have already checked whether $n$ is divisible by $b$. To speed things up even further, we may exploit the fact that after 2, we can skip the other even numbers. So, 2 and the odd numbers may be used as trial divisors.

As a slightly tighter upper bound we only need to check upto $\sqrt{n}$ which can be proved by the following theorem. 

```{prf:theorem}
If $n > 1$ is composite, then $n$ has a prime divisor $p$ such that $p \le \sqrt{n}$
```

`````{prf:proof}

If $n$ is composite, then $n = ab$ where $a > 1$ and $b > 1$. For convenience suppose $a\le b$. 

Let $p$ be a prime divisor of a. Thus, $p \le a \le b$. So

```{math}
p^2 \le a^2 \le ab = n
```

Since, $p | a$ and $a | n$ we have $p | n$.
`````

Therefore, the algorithm can be summarized as follows:

```{prf:algorithm}
**Input:** Integer $n > 1$

1. If $2 | n$ return COMPOSITE
2. Take $k = 3$
3. while $k^2 \le n$ do
  1. if $k | n$ return COMPOSITE
  2. else $k = k + 2$ and repeat the loop
4. return PRIME
```

We can also use sieving techniques, that way our trial divisors will only be the prime numbers upto $\sqrt{n}$.

## Theoretical Considerations

Suppose we wish to use trial division to test $n$ for primality. 

The worst case running time is when $n$ is prime and we must try all potential divisors i.e., the numbers up to $\sqrt{n}$. If we are using just primes as trial divisors, the number of divisions is about $2 \frac{\sqrt{n}}{ln n}$.

<!--  -->

If we use 2 and the odd numbers as trial divisors, the number of
divisions is about 1
2
√n. 

So this is the running time for trial division as a primality test. What is its
complexity as an algorithm to obtain the complete factorization of n when n is
composite? The worst case is still about √n, for just consider the numbers that
are the double of a prime. We can also ask for the average case complexity for
factoring composites. Again, it is almost √n, since the average is dominated
by those composites that have a very large prime factor. But such numbers are
rare. It may be interesting to throw out the 50% worst numbers and compute
the average running time for trial division to completely factor the remaining
numbers. This turns out to be nc, where c = 1/(2√e) ≈ 0.30327; see Exercise
3.5.
As we shall see later in this chapter and in the next chapter, the problem
of recognizing primes is much easier than the general case of factorization. In
particular, we have much better ways than trial division to recognize primes.
Thus, if one uses trial division as a factorization method, one should augment
it with a faster primality test whenever a new unfactored portion of n is
discovered, so that the last bit of trial division may be skipped when the
last part turns out to be prime. So augmenting trial division, the time to
completely factor a composite n essentially is the square root of the second
largest prime factor of n.
Again the average is dominated by a sparse set of numbers, in this case
those numbers that are the product of two primes of the same order of
magnitude; the average being about √n. But now throwing out the 50% worst
numbers gives a smaller estimate for the average of the remaining numbers.
It is nc, where c ≈ 0.23044.