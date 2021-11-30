# RSA

## Modular Inversion

We say $x$ is multiplicative inverse of $a$ modulo $N$ if $ax \equiv 1 (mod N)$.
This has a solution only when $(a, N) = 1$ otherwise the remainder will never be 1 (remainder will always be a multiple of gcd).

### Modular division theorem
For any a mod N, a has a multiplicative inverse modulo N if and only if it is relatively prime to N. When the inverse exists it can be found in O(n^3) (n is the number of bits of N) by running extended Euclid algorithm.

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