"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

https://projecteuler.net/problem=23
"""


import argparse
import utils

from itertools import product


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='Find the sum of all the positive integers which cannot be written as the sum of two abundant '
                    'numbers.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    nums = utils.sum_divisors(28123)
    abundant_nums = {i: nums[i] for i in nums.keys() if i < nums[i]}
    sums = {i + j for i, j in product(abundant_nums, abundant_nums) if j >= i and i + j <= 28123}
    print(utils.sum_series(28123) - sum(sums))


if __name__ == '__main__':
    main()