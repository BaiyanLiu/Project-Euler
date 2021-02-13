"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5
"""


import argparse

from functools import reduce
from operator import mul
from sys import maxsize
from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive).')
    return parser.parse_args()


def main():
    args = get_args()
    step = reduce(mul, sieve(args.n))
    nums = range(1, args.n + 1)
    print(next(i for i in range(step, maxsize, step) if all([i % j == 0 for j in nums])))


if __name__ == '__main__':
    main()
