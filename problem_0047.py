"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

https://projecteuler.net/problem=47
"""


import utils

from itertools import count


def main():
    primes = utils.sieve(5000)
    num_factors = [len(utils.num_factors(i, primes)) for i in range(210, 214)]
    for i in count(214):
        num_factors.append(len(utils.num_factors(i, primes)))
        if all(j == 4 for j in num_factors[-4:]):
            print(i - 3)
            break


if __name__ == '__main__':
    main()
