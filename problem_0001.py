"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the sum of all the multiples of a or b below n.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('a', type=int, help='First number.')
    parser.add_argument('b', type=int, help='Second number.')
    parser.add_argument('n', type=int, help='Upper limit (exclusive).')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum(multiples(args.a, args.n) | multiples(args.b, args.n)))


def multiples(x: int, n: int) -> set[int]:
    return set(range(x, n, x))


if __name__ == '__main__':
    main()
