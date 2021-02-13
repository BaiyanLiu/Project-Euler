"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1,
2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

https://projecteuler.net/problem=24
"""


import argparse

from utils import factorial_series


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the nth lexicographic permutation of the digits 0 to x?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Permutation number')
    parser.add_argument('x', type=int, help='Upper limit (inclusive)')
    args = parser.parse_args()
    args.n -= 1
    return args


def main():
    args = get_args()
    factorials = list(reversed(factorial_series(args.x)))
    nums = list(range(args.x + 1))
    # If there's 10 digits, then 0 is the first digit of the first 9! permutations
    print(''.join([str(nums.pop(args.n // factorials[i] % len(nums))) for i in range(args.x + 1)]))


if __name__ == '__main__':
    main()
