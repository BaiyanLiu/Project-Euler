"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6
"""


import argparse

import utils


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the difference between the sum of the squares of the first n natural numbers and the square '
                    'of the sum.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive).')
    return parser.parse_args()


def main():
    args = get_args()
    square_of_sum = utils.sum_series(args.n) ** 2
    sum_of_squares = sum(utils.square_nums(1, args.n + 1))
    print(square_of_sum - sum_of_squares)


if __name__ == '__main__':
    main()
