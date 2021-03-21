"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2
to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

https://projecteuler.net/problem=26
"""


import argparse

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the value of d < n for which 1/d contains the longest recurring cycle in its decimal '
                    'fraction part.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    max_cycle, max_num = 0, 0
    for num in sieve(args.n):
        cycle, digit, first_digit = 0, 1, None
        while (cycle := cycle + 1) and (digit := digit % num * 10):
            if first_digit is None:
                first_digit = digit
                continue
            elif first_digit != digit:
                continue
            if cycle > max_cycle:
                max_cycle, max_num = cycle, num
            break
    print(max_num)


if __name__ == '__main__':
    main()
