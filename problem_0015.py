import argparse

from functools import reduce
from operator import mul


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many such routes are there through a n×n grid?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The size')
    return parser.parse_args()


def main():
    args = get_args()
    num = reduce(mul, range(args.n + 1, args.n * 2 + 1))
    denom = reduce(mul, range(2, args.n + 1))
    print(num // denom)


if __name__ == '__main__':
    main()
