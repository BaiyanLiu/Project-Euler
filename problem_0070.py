"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive
numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
than nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

https://projecteuler.net/problem=70
"""


from sys import maxsize

import utils


def main():
    limit = 10000000
    primes = utils.sieve(limit // 2)
    min_n, min_v = 0, maxsize
    for i in primes:
        for j in primes:
            if (n := i * j) > limit:
                break
            phi = (i - 1) * (j - 1)
            if (v := n / phi) < min_v and utils.is_permutation(n, phi):
                min_n, min_v = n, v
    print(min_n)


if __name__ == '__main__':
    main()