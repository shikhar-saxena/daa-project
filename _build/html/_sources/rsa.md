# RSA

### Euclid's Algorithm

Euclid's algorithm is a simple algorithm stated as follows:

```
function Euclid(a, b) 

Input: Two integers a and b with a >= b >= 0
Output: gcd(a, b)

if b = 0: return a
return Euclid(b, a mod b) 
```

This algorithm is based on the divide and conquer paradigm (the property used here for recursion is proved later). In Euclid's algorithm we see, that we reduce the second operand (because `a mod b` will always be less than `b`). Eventually the second operand will turn 0 which is our base case i.e., GCD(a, 0) is a (since 0 is divisible by any number).

Thus the reduction of 2nd operand eventually leads the algorithm to terminate. Analysis of this algorithm is shown later.

The property used for recursion is stated as follows:

> If x and y are positive integers with x >= y then `gcd(x, y) = gcd(x mod y, y)`

**Proof:**

It is enough to show the slightly simpler rule `gcd(x, y) = gcd(x - y, y)` from which the one stated can be derived by repeatedly subtracting y from x (since `x mod y` is `x - ny` for some `n`).

Any integer that divides both x and y must also divide x - y so gcd(x, y) must also be a common divisor of gcd(x - y, y). Likewise, any integer that divides both x - y and y also divides x and y. Thus, gcd(x - y, y) is also a common factor of gcd(x, y). Thus, `gcd(x, y) = gcd(x - y, y) = gcd(x mod y, y)`

#### Analysis

**Lemma:** If a >= b then a mod b < a/2.

**Proof:**

Either b <= a/2 or b > a/2. For these two cases we notice:

- if b <= a/2 then we have a mod b < b <= a/2
- and if b > a/2 then a mod b = a - b < a/2

So no matter the values of a and b, two steps in recursion (one comparison and one computation a mod b) our input gets halved.

Therefore, for 2k steps a, will be reduced to a/2^k.

Therefore total steps required will be about `2 log a` steps. Therefore this algorithm will work for larger numbers as well (since it is logarithmic in time).

Therefore for n-bit numbers a and b it will take O(n) time which is linear in time. Thus, this algorithm is an optimum algorithm.


### Extended Euclid's Algorithm

Extended Euclid's algorithm solves a generalization of GCD.

**Lemma** If d divides both `a` and `b` and `d = ax + by` where x and y are some integers then necessarily `d = gcd(a, b)`.

Thus the lemma states that the number that divides both a and b, that can be expressed as their linear combination, is the gcd of the two numbers.

**Proof**: By the first two conditions d is a common divisor of a and b and so it cannot exceed the greatest common divisor, that is, `d <= gcd(a, b)`. On the other hand since gcd(a, b) is a common divisor of a and b, it must also divide `ax + by = d` which implies `gcd(a,b) <= d`. So from these two inequalities we get

`d = gcd(a, b)`

Therefore Extended Euclid's algorithm tries to find such coefficients x and y so as to compute the GCD. Thus, this is a generalization of GCD. We not just find the GCD but we also find out coefficients associated with each input a and b.

#### How to find such x and y?

**Example**
For gcd(25, 11)

Euclid's algorithm proceeds as follows

```
25 = 2.11 + 3
11 = 3.3 + 2
3 = 1.2 + 1
2 = 2.1 + 0
```


> Essentially gcd(25, 11) = gcd(25 mod 11, 11) = gcd(3, 11) = gcd(3, 2) = gcd(1, 2) = gcd(1, 0) = 1

This gives us an idea to find coefficients x and y. 

25 can be written as a linear combination of 11 and 3 or in other words linear combination of 25 and 11 give 3. But 3 itself can be written as a  combination of 2 and 1 where 2 is given as a combination of 1 (and 0).

Thus, we reach 1 as a linear combination of 25 and 11.

#### Algorithm

```
function extended-Euclid(a, b)

Input: Two positive integers a and b with a >= b >= 0
Output: Integers x, y, d such that d = gcd(a, b) and ax + by = d

if b = 0 return (1, 0, a)
(x', y', d) = extended-Euclid(b, a mod b)

return (y', x' - \lfloor a/b \rfloor y', d)
```

Here we use the division property:
Dividend = Quotient * Divisor + Remainder

So,
```
a = (\lfloor a/b \rfloor) * b + a mod b 
or a mod b = a - (\lfloor a/b \rfloor) * b
```

Substituting this value of a mod b we can get the desired combination for a and b.

## Modular Inversion

We say $x$ is multiplicative inverse of $a$ modulo $N$ if $ax \equiv 1 (mod N)$.
This has a solution only when $(a, N) = 1$ otherwise the remainder will never be 1 (remainder will always be a multiple of gcd).

The multiplicative inverse of a number $a$ such that $(a, N) = 1$ can be found by running extended Euclid algorithm in $O(n^3)$.

Thus continuing with our previous example we wish to compute 11^{-1} mod 25.
Using extended Euclid algorithm we find that 15. 25 - 34.11 = 1.

Reducing both sides modulo 25 we have `-34.11 \equiv 1 (mod  25)`

So -34 \equiv 16 mod 25 is the inverse of 11 mod 25.

## Public Key cryptography

Main Question in Public Key cryptography is if we publish our key how can we still maintain security.

The answer lies in representation. The key can be represented in different ways. Thus the representation we share with the world is different from the one on our local machines.

Thus, we think of two representations: public and private key which are the encryption and the decryption key respectively. The encryption algorithm runs very fast in the public key but decryption algorithm is very slow which runs faster in the private key.

### Ease/Speed of operation depends on representation

We can represent numbers in their prime factorization, as decimals, or as in roman numeral form.

![representation](./img/representation.png)

We can write/compute product of numbers faster in prime factor representation. (Only exponent addition to compute multiplication). Thus this representation is the best for multiplication.

For addition however the decimal representation is the best. Comparison for instance is moderate in decimals but slightly less moderate in prime factorization form.

Roman representation on the other hand is slow in all three operations. Slowness is actually advantageous because decryption will be slow for such a representation.

![operation](./img/operation.png).

Binary representation is faster for comparison and addition but not for multiplication.

### RSA Cryptosystem
So we represent the key in two forms R_1 and R_2 essentially one representation has faster encryption (public) and the other one has faster decryption (private).

Here, the algorithms depend on the representation utilized for cryptography.

### RSA

Pick any two primes p and q and let N = p * q
For any e relatively prime to (p - 1)(q - 1) the mapping f(x) =  x^e mod N is a bijection on {0, 1, ..., N-1} 
Moreover, the inverse mapping is easily realized: let d be the inverse of e modulo (p -1)(q - 1). 

Then for all x in {0,..., N-1} 

`(x^e)^d mod N = x mod N`

#### RSA Correctness

$$x^{ed} - x = x^{ 1 + k(p - 1)(q - 1) } - x$$

This is always 0 modulo N. which we will show from Fermat's little theorem.

##### Fermat's little theorem
If p is prime then for every 1 <= a < p,
$$ a^{p - 1} \equiv 1 (mod p)$$

**Proof**

We assume $i \in {1,2,..., p - 1}$.

The numbers a.i mod p are distinct because if $a.i \equiv a.j (mod p)$ then dividing both sides by a gives $i \equiv j (mod p)$. They are nonzero because $a.i \equiv 0$ similarly implies $i \equiv 0$. (and we can divide by a so we assume a is nonzero and therefore relatively prime to p).

Thus,
`{1,2,..., p - 1} = {a . 1 mod p, a . 2 mod p,..., a . (p - 1) mod p}`


If we multiply together its elements in each of these representations we get
$$(p - 1)! \equiv a^{p - 1} . (p - 1)! (mod p)$$

Dividing each side by $(p - 1)!$ we get the proof to our theorem.

#### RSA correctness revisited
The second form of the expression is convenient when simplified using Fermat's theorem. It is divisible by p (since $x^{p - 1} \equiv 1 mod p$) and likewise by q. Since p and q are primes, this expression thus becomes divisible by their product N. Hence, RSA is proved.