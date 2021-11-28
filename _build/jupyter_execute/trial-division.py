#!/usr/bin/env python
# coding: utf-8

# # Trial Division Test
# 
# ```{prf:theorem}
# Let $n > 1$ be an integer. Then n has no prime divisor less than or equal to $\sqrt{n}$ if and only if $n$ is prime.
# ```
# 
# ```{prf:proof}
# 
# If $n$ is composite, then $n = ab$ where $a > 1$ and $b > 1$. For convenience suppose $a\le b$. 
# 
# Let $p$ be a prime divisor of a. Thus, $p \le a \le b$. So
# 
# $p^2 \le a^2 \le ab = n$
# 
# Since, $p | a$ and $a | n$ we have $p | n$.
# ```
# 
# ## Divisibility Test
# 
# A divisibility test is a procedure applied to a number $n$ so as to determine whether $n$ is divisible by a particular small number or not. 
# 
# From a computational point of view, checking if $n$ is divisible by a number $p$ can be achieved by dividing $n$ by $p$ and getting the quotient and remainder. For remainder being 0, the number is said to be divisible and $p$ is said to be a *factor* of $n$.
# 
# **Trial Division** is the most laborious but easiest to understand of the integer factorization algorithms.
# 
# We sequentially check whether *n* is divisible or not by the members of the set of trial divisors for *n*. 
#  <!--TODO: FIXME:  -->
# 
# It is not necessary that the trial divisors be all primes. To speed things up, however we may exploit the fact that after 2, we can skip the other even numbers. So, 2 and the odd numbers may be used as trial divisors.
