# Probabilistic Primality Testing

Probabilistic tests are randomized algorithms. They are more rigorous in that they provide provable bounds on the probability of being fooled by a composite number. 

Many popular primality tests are probabilistic tests. These tests use, apart from the tested number $n$, some other numbers $a$ which are chosen at random from some sample space.

The usual randomized primality tests never report a prime number as composite, but it is possible for a composite number to be reported as prime. The probability of error can be reduced by repeating the test with several independently chosen values of $a$; for example, for any composite $n$ if at least half the $a$'s detect $n$'s compositeness, so with $k$ repetitions, we can reduce the error probability to at most $2^{-k}$, which can be made arbitrarily small by increasing $k$.

The basic structure of randomized primality tests is as follows:
- Randomly pick a number $a$.
- Check equality (corresponding to the chosen test) involving $a$ and the given number $n$. If the equality fails to hold true, then $n$ is a composite number and $a$ is a witness for the compositeness, and the test stops.
- Get back to the step one until the required accuracy is reached.

After one or more iterations, if $n$ is not found to be a composite number, then it can be declared probably prime.

<!-- !!!
As we have seen in the previous two sections it is theoretically very straightforward,
using either the direct method of trial division or the sieve of Eratosthenes, to test an
integer for primality. The problem is that for large integers $n$ these methods become
computationally intractable if not almost impossible. Hence direct trial division and
the sieve of Eratosthenes can be used only for relatively small integers, and therefore
for large integers other methods must be employed. We should note before going
further that the concepts of small and large are very relative in number theory to
the type of computing machinery one is using. Numbers as large as 10,000,000,000
can be tested very easily, even on small computers, using the sieve of Eratosthenes.
In terms of computational asymptotic number theory, 109 is still small. Similarly,
for human computation the total number of atoms in the universe is massive. This
number is estimated as being on the order of 1079. However, 79 digit integers are
considered only moderate in asymptotic computational number theory, which may
want to handle integers with hundreds or even thousands of digits. Therefore what is
needed are tests for primality that will handle some of these gigantic integers.
A primality test is then an algorithm that inputs a positive integer n and outputs
whether it is prime or composite. These tests can be sub-classified as either deterministic primality tests or probabilistic primality tests. In a deterministic test an
integer n is inputted and the output is, yes the integer is prime, or no the integer is not
prime. Hence both the direct method of trial division and the sieve of Eratosthenes
are deterministic tests. A nondeterministic primality test takes an inputted integer n and returns either no it
is not prime or it may be a prime. A probabilistic primality test is a nondeterministic
test that returns either that the inputted integer is not a prime or that is probably a
prime to some given degree of likelihood. There are various tests (that we will look
at in the next section) that can give this likelihood to as high a probability as desired.
Numbers that pass a probabilistic primality test are called probable primes. For use
in cryptography, knowing whether an integer is prime to a high probability is often
just as good as knowing if it is definitely prime. For this reason, probable primes with
a high degree of probability are called industrial grade primes, a term originally
coined by M. Cohen. -->