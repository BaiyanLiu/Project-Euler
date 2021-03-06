"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If
this process is continued, what is the side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

https://projecteuler.net/problem=58
"""


from itertools import count
from math import sqrt
from utils import sieve


def main():
    primes = sieve(100000)
    num_primes = 0
    for i in count(3, 2):
        i2 = i ** 2
        num_primes += sum(1 for k in (i2 - (i - 1) * j for j in range(1, 4)) if is_prime(k, primes))
        if num_primes / (i * 2 - 1) < 0.1:
            print(i)
            break


def is_prime(n: int, primes: list[int]) -> int:
    """https://en.wikipedia.org/wiki/Primality_test"""
    if n < 2:
        return False
    limit = sqrt(n)
    for prime in primes:
        if prime > limit:
            break
        if n % prime == 0:
            return False
    return True


if __name__ == '__main__':
    main()
