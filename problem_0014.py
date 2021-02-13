"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

https://projecteuler.net/problem=14
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Which starting number, under n, produces the longest Collatz chain?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    nums = {1: 1}
    for i in range(2, args.n):
        collatz(i, nums)
    print(max(nums, key=nums.get))


def collatz(n: int, nums: dict[int, int]) -> int:
    if n not in nums:
        nums[n] = collatz(n // 2 if n % 2 == 0 else n * 3 + 1, nums) + 1
    return nums[n]


if __name__ == '__main__':
    main()
