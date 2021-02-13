"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7
"""


import argparse
import math

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the nth prime number?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The number.')
    return parser.parse_args()


def main():
    args = get_args()
    primes = sieve(rosser(args.n))
    print(primes[args.n - 1])


def rosser(n: int) -> int:
    """https://en.wikipedia.org/wiki/Rosser's_theorem"""
    return n * math.ceil(math.log(n) + math.log(math.log(n)))


if __name__ == '__main__':
    main()
