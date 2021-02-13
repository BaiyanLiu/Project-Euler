"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

https://projecteuler.net/problem=37
"""


import argparse
import re

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='Find the sum of the only eleven primes that are both truncatable from left to right and right to '
                    'left.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    primes = sieve(1000000)
    all_primes = list(map(str, primes))
    pattern = re.compile('^[2357][1379]*[37]$')
    candidate_primes = [str(p) for p in primes if re.match(pattern, str(p))]
    sums = 0
    for prime in candidate_primes:
        if all([prime[i:] in all_primes and prime[:i] in all_primes for i in range(1, len(prime))]):
            sums += int(prime)
    print(sums)


if __name__ == '__main__':
    main()
