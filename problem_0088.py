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
