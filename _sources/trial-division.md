---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Trial Division Test

**Trial Division** is the most laborious yet easiest to understand of the integer factorization algorithms.

### Method

Given an integer $n$, the trial division consists of sequentially testing whether $n$ is divisible by any smaller number. Clearly, it is only worthwhile to test factors less than $n$, and in order from two upwards (since two is the first prime number). With this ordering, there is no point in testing for divisibility by four if the number has already been determined not divisible by two, and so on for three and any multiple of three, etc. Therefore, the effort can be reduced by selecting only prime numbers as test divisors. Furthermore, the test divisors need go no further than $\sqrt {n}$ because, if $n$ is divisible by some number $p$, then $n = p \times q$ and if $q$ were smaller than $p$, $n$ would have been detected earlier as being divisible by $q$ or by a prime factor of $q$.

We can augment trial division test to do primality testing as follows: 

**Factor $n$ using trial division test. $n$ is prime if and only if none of the trial divisors divides n.**


It is not necessary that the trial divisors be all primes. To speed things up, however we may exploit the fact that after 2, we can skip the other even numbers. So, 2 and the odd numbers may be used as trial divisors.



<!-- An integer n is composite if n > 1 and n is not
prime. (The number 1 is considered neither prime nor composite.) Thus,
an integer n is composite if and only if it admits a nontrivial factorization
n = ab, where a, b are integers, each strictly between 1 and n. Though the
definition of primality is exquisitely simple, the resulting sequence 2, 3, 5, 7,...
of primes will be the highly nontrivial collective object of our attention. The
wonderful properties, known results, and open conjectures pertaining to the
primes are manifold. We shall cover some of what we believe to be theoretically
interesting, aesthetic, and practical aspects of the primes. Along the way,
we also address the essential problem of factorization of composites, a field
inextricably entwined with the study of the primes themselves.
In the remainder of this chapter we shall introduce our cast of characters,
the primes themselves, and some of the lore that surrounds them. -->

```{prf:theorem}
Let $n > 1$ be an integer. Then $n$ has no prime divisor less than or equal to $\sqrt{n}$ if and only if $n$ is prime.
```

`````{prf:proof}

If $n$ is composite, then $n = ab$ where $a > 1$ and $b > 1$. For convenience suppose $a\le b$. 

Let $p$ be a prime divisor of a. Thus, $p \le a \le b$. So

```{math}
p^2 \le a^2 \le ab = n
```

Since, $p | a$ and $a | n$ we have $p | n$.
`````

## Divisibility Test

A divisibility test is a procedure applied to a number $n$ so as to determine whether $n$ is divisible by a particular small number or not. 

From a computational point of view, checking if $n$ is divisible by a number $p$ can be achieved by dividing $n$ by $p$ and getting the quotient and remainder. For remainder being 0, the number is said to be divisible and $p$ is said to be a *factor* of $n$.

**Trial Division** is the most laborious but easiest to understand of the integer factorization algorithms.

We sequentially check whether *n* is divisible or not by the members of the set of trial divisors for *n*. 
 <!--TODO: FIXME:  -->

It is not necessary that the trial divisors be all primes. To speed things up, however we may exploit the fact that after 2, we can skip the other even numbers. So, 2 and the odd numbers may be used as trial divisors.