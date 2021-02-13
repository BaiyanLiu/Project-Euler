"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

https://projecteuler.net/problem=30
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the sum of all the numbers that can be written as the sum of nth powers of their digits.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The power')
    return parser.parse_args()


def main():
    args = get_args()
    powers = {str(i): i ** args.n for i in range(10)}
    i, max_num = 9, powers['9']
    while (i := i * 10 + 9) < (max_num := max_num + powers['9']):
        pass
    print(sum([i for i in range(2, max_num) if sum([powers[c] for c in str(i)]) == i]))


if __name__ == '__main__':
    main()
