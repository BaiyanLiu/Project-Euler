"""
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1,
a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal
product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in
the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

https://projecteuler.net/problem=88
"""


import argparse
import sys
from functools import reduce
from operator import mul
from sys import maxsize


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the sum of all the minimal product-sum numbers for 2≤k≤n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    sys.setrecursionlimit(args.n * 2)
    nums = {i: maxsize for i in range(2, args.n + 1)}

    for i in range(2, args.n + 1):
        find_nums(nums, [i], i, args.n)

    print(sum(set(nums.values())))


def find_nums(nums: dict[int, int], digits: list[int], curr_digit: int, n: int) -> None:
    product = reduce(mul, digits, 1) * curr_digit
    num_digits = len(digits) + product - sum(digits) - curr_digit + 1

    if num_digits > n:
        return

    find_nums(nums, digits, curr_digit + 1, n)
    find_nums(nums, digits + [curr_digit], curr_digit, n)

    if product < nums[num_digits]:
        nums[num_digits] = product


if __name__ == '__main__':
    main()
