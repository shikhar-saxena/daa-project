# Miller-Rabin Primality Test

Prime = "On input p:

1. If p is even, accept if p = 2; otherwise reject.
2. Select $a_1, a_2, ..., a_k$ randomly in $Z_p^+$.
3. For each i from 1 to k:
4.  Compute $a_i^{p - 1}$ mod p and reject if different from 1.
5.  Let $p - 1 = st$ where s is odd and $t = 2^h$ is a power of 2
6.  Compute the sequence $a_i^{s 2^0}, a_i^{s 2^1},..., a_i^{s 2^h}$ modulo p.
7.  If some element of this sequence is not 1 find the last element that is not 1 and reject if that element is not -1.
8. All tests have passed at this point so accept."

There's a very less probable chance that the number is composite and the algorithm accepts it as prime.

In step `4` we know by Fermat's Little Theorem, that for prime numbers the remainder will be 1. Of course there can be composite numbers with remainder as 1 (for which we do the further steps). Thus, here we eliminate the number if its remainder is not 1.

Since `p` is odd at this point so `p - 1` is even and is assumed to be `st` where `s` and `t` are assumed as above.

Now, we start from 0 as the power of 2 and go on till $2^h = t$ and for each we check $a_i^{s 2^h}$ modulo p. We know this sequence always ends at 1 (we calculated this in step `4`). This sequence will have all terms from 1 to p - 1 (since 0 is not possible by this step). We read the sequence from right to left. If some element of this sequence is not 1 we reject if that element is not -1.

### Proof

If p is prime then algorithm will always accept. In step 4, it will always give 1 due to Fermat's little theorem and here it will never reject. Next it may reject at step 7.

We prove that the first number (reading from right to left) that is not 1 will be -1 for a prime input.

Notice that last number is 1. And the element before it is the square root of this number. And every previous element is the square root of the next element.

So let's say we encounter the element `b` whose modulo is not 1.

Therefore, $b \not \equiv 1 (\text{mod} p)$ and $b^2 \equiv 1 (\text{mod} p)$.

$$\implies b^2 - 1 \equiv 0 (\text{mod} p)$$
$$\implies (b - 1)(b + 1) \equiv 0 (\text{mod} p)$$

By Euclid's lemma,
> If a prime p divides the product ab of two integers a and b, then p must divide at least one of those integers a and b.

which means that if p is prime it divides one of the factors `b - 1` or `b + 1`, implying that b is congruent to either 1  or -1 modulo n.
From our assumption, therefore $b \equiv -1 (mod n)$.

This explains step `7` in our algorithm. If all tests are passed then we accept it.

Therefore, Probability(Algorithm accepts prime numbers) = 1.

### For Composite Numbers

If `p` is an odd composite number and `a` is selected randomly in $Z_p^+$, then we prove that Probability(a is a witness) >= 1/2 by demonstrating that at least as many witnesses as non witnesses exist in $Z_p^+$.

Here, witness means that `a` confirms that `p` is composite (from the Miller-Rabin Test). And non-witness means that `a` gives prime for `p` when `p` is composite.

#### Proof

In every non witness, the sequence computed in stage 6 is either all 1s or contains -1 at some location followed by 1s. For example, 1 itself is a non witness of the first kind and -1 is a non witness of the second kind since s is odd and $(-1)^{s 2^0} \equiv -1$ and $(-1)^{s 2^1} \equiv 1$.

Among all these non-witnesses, we consider h to be the non witness where -1 appears at the rightmost position in the sequence and let that position be j (positions numbered from 0). Hence, $h^{s 2^j} \equiv -1$ (mod p).

Because p is composite, either p is exact prime power or it has atleast two prime factors and we can write it as product of `q` and `r`, which are relatively prime. We consider the latter case first. Therefore by the Chinese remainder theorem, some number t exists in $Z_p$ such that
```
t \equiv h (mod q) and
t \equiv 1 (mod r)
```

Therefore,
```
t^{s 2^j} \equiv -1 (mod q)
t^{s 2^j} \equiv  1 (mod r)
```
Hence, t is a witness because $t^{s 2^j} \not \equiv \pm 1$ (mod p) but $t^{s 2^{j + 1}} \equiv 1$ (mod p).

Since, $t^{s 2^{j + 1}} \equiv 1$ for both mod q and mod r thus it will also hold for mod p. But at j^th location it is -1 for mod q and 1 for mod r. Therefore, it cannot be $\pm 1$ for mod p. Thus t will becomes a witness in this case.

Now, that we have one witness we can show that $dt mod p$ is a unique witness for each non witness d by making two more observations:

First, $d^{s 2^j} \equiv \pm 1$ (mod p) and $d^{s 2^{j + 1}} \equiv 1$ (mod p) owing to the way j was chosen. Therefore `dt mod p` is a witness because $(dt)^{s 2^j} \not \equiv \pm 1$ (mod p) and $(dt)^{s 2^{j + 1}} \equiv 1$ (mod p).

Second, d_1 and d_2 are distinct non witnesses, d_1 t mod p not equal to d_2 t mod p. The reason is that $t^{s 2^{j + 1}}$ mod p = 1. Hence, $t.t^{s 2^{j + 1} - 1}$ mod p = 1. Therefore, if t d_1 mod p = t d_2 mod p, then

$d_1 = t.t^{s 2^{j + 1} - 1} d_1 mod p = t.t^{s 2^{j + 1} - 1} d_2 mod p = d_2$.

Thus, the number of witnesses must be as large as the number of non witnesses and we have completed the analysis for the case where p is not a prime factor.


For the prime power case we have p = q^e where q is prime and e > 1. Let t = 1 + q^{e - 1}. Expanding t^p using the binomial theorem we obtain

$t^p = (1 + q^{e - 1})^p = 1 + p q^{e - 1}$ + multiples of higher powers of q^{e - 1} which is congruent to 1 mod p. Hence, t is a stage for witness because if t^{p − 1} \equiv 1 (mod p), then $t^p \equiv t \not \equiv 1$ (mod p). As in the previous case, we use this one witness to get many others. If d is a non witness we have d^{p - 1} \equiv 1 (mod p) but then dt mod p is a witness. Moreover if d_1 and d_2 are distinct non witnesses, then d_1 t mod p not equal to d_2 t mod p. Otherwise,

$d_1 = d_1 t t^{p - 1} mod p = d_2 t t^{p - 1} mod p = d_2$.

Thus the number of witnesses must be as large as the number of non-witnesses and the proof is complete.
