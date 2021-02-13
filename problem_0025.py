"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

https://projecteuler.net/problem=25
"""


import argparse
import math


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the index of the first term in the Fibonacci sequence to contain n digits?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of digits')
    return parser.parse_args()


def main():
    args = get_args()
    phi = (1 + math.sqrt(5)) / 2
    # 10 ^ (n - 1) < phi ^ n / sqrt(5)
    print(math.ceil((math.log10(10) * (args.n - 1) + math.log10(5) / 2) / math.log10(phi)))


if __name__ == '__main__':
    main()
