# Probabilistic Primality Testing

Probabilistic tests are randomized algorithms. They are more rigorous in that they provide provable bounds on the probability of being fooled by a composite number. 

Many popular primality tests are probabilistic tests. These tests use, apart from the tested number $n$, some other numbers $a$ which are chosen at random from some sample space.

The usual randomized primality tests never report a prime number as composite, but it is possible for a composite number to be reported as prime. The probability of error can be reduced by repeating the test with several independently chosen values of $a$; for example, for any composite $n$ if at least half the $a$'s detect $n$'s compositeness, so with $k$ repetitions, we can reduce the error probability to at most $2^{-k}$, which can be made arbitrarily small by increasing $k$.

The basic structure of randomized primality tests is as follows:
- Randomly pick a number $a$.
- Check equality (corresponding to the chosen test) involving $a$ and the given number $n$. If the equality fails to hold true, then $n$ is a composite number and $a$ is a witness for the compositeness, and the test stops.
- Get back to the step one until the required accuracy is reached.

After one or more iterations, if $n$ is not found to be a composite number, then it can be declared probably prime.

## Note on Randomized Algorithms

Often times no efficient deterministic algorithm is known to a problem. This is when randomized algorithms are useful. 

In randomized algorithms, we essentially take some random step as our next step. At first glance it seems haphazard because the algorithm does not know what to run beforehand and it may not be useful. But Randomized algorithms are far from this and are often useful. Rather than viewing it from the designer's perspective we view it from the adversaries' perspective (i.e., what sort of input can be the worst case input). Since its a randomized algorithm, the notion of worst case input is difficult to pinpoint. That's why randomized algorithms can be useful.

Example: Quick sort

If we choose a deterministic quick sort we can always give an input which does not split the input evenly in the recursion step and can take $O(n^2)$. Rather if we take a random pivot each time (randomized quick sort) it may become more efficient i.e, $O(n log n)$.

We can also understand randomized algorithms this way: 

We create several efficient algorithms for the problem $A_1, A_2, ..., A_k$ such that for any input there are at least $2k/3$ values of $i$ such that the algorithm $A_i$ correctly solves the problem. So for any input atleast two-thirds of our set of algorithms will be able to solve the problem. This way however we may not terminate unless we compute each algorithm in our set. So we choose three algorithms randomly from the set and take the majority solution.