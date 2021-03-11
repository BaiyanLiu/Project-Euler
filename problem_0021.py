"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) =
b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

https://projecteuler.net/problem=21
"""


import argparse

from utils import sum_divisors


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Evaluate the sum of all the amicable numbers under n.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    sums = sum_divisors(args.n)
    print(sum([i for i in sums if sums[i] != i and sums[i] in sums and sums[sums[i]] == i]))


if __name__ == '__main__':
    main()
