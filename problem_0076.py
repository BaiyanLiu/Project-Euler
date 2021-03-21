"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

https://projecteuler.net/problem=76
"""


import argparse

from utils import pentagonal_nums


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many different ways can n be written as a sum of at least two positive integers?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The number')
    return parser.parse_args()


def main():
    args = get_args()
    pen_nums = sorted(pentagonal_nums(-args.n, args.n + 1))
    pen_nums.remove(0)
    print(num_partitions(args.n, pen_nums, {}) - 1)


def num_partitions(n: int, pen_nums: list[int], partitions: dict[int, int]) -> int:
    """https://en.wikipedia.org/wiki/Partition_(number_theory)"""
    if n == 0:
        return 1
    if n not in partitions:
        partitions[n] = 0
        for i in range(len(pen_nums)):
            if (prev_n := pen_nums[i]) > n:
                break
            partitions[n] += num_partitions(n - prev_n, pen_nums, partitions) * (-1 if i // 2 % 2 == 1 else 1)
    return partitions[n]


if __name__ == '__main__':
    main()
