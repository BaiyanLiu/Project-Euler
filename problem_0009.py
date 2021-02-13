"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the Pythagorean triplet product abc for which a + b + c = n.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The sum')
    return parser.parse_args()


def main():
    args = get_args()
    for a in range(1, args.n // 3):
        a2 = a ** 2
        for b in range(a + 1, args.n // 2):
            if (c := args.n - a - b) ** 2 == a2 + b ** 2:
                print(a * b * c)
                exit()


if __name__ == '__main__':
    main()
