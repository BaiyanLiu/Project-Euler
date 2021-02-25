"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

https://projecteuler.net/problem=16
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the sum of the digits of the number n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The number')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum(map(int, str(args.n))))


if __name__ == '__main__':
    main()
