"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (
i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

https://projecteuler.net/problem=49
"""


import argparse

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='What 12-digit number do you form by concatenating the three terms in this sequence?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    primes = set([p for p in sieve(10000) if p >= 1000 and p not in {1487, 4817, 8147}])
    for i in primes:
        for j in [p for p in primes if p > i]:
            if (k := j + j - i) in primes and sorted(str(i)) == sorted(str(j)) == sorted(str(k)):
                print(f'{i}{j}{k}')
                break


if __name__ == '__main__':
    main()
