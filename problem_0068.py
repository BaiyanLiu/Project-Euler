"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
p068_1.png

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,
2 in this example), each solution can be described uniquely. For example, the above solution can be described by the
set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is
the maximum 16-digit string for a "magic" 5-gon ring?
p068_2.png

https://projecteuler.net/problem=68
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Using the numbers 1 to 2n, and depending on arrangements, What is the maximum d-digit string for '
                    'a "magic" n-gon ring?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('d', type=int, help='Number of digits')
    parser.add_argument('n', type=int, help='Size of ring')
    return parser.parse_args()


def main():
    args = get_args()
    nums = list(range(1, 2 * args.n + 1))
    print(max_ring_value([], nums, args.d))


def max_ring_value(nums: list[int], candidates: list[int], digits: int) -> int:
    if len(nums) == len(candidates):
        return int(arranged) if len(arranged := arrange_nums(nums)) == digits else 0
    else:
        max_value = 0
        for c in [c for c in candidates if c not in nums]:
            if len(nums) >= 4:
                sum_group = nums[0] + nums[1] + nums[2]
                if len(nums) == len(candidates) - 1:
                    if c + nums[-1] + nums[1] != sum_group:
                        continue
                elif len(nums) % 2 == 0 and c + nums[-1] + nums[-2] != sum_group:
                    continue
            max_value = max(max_value, max_ring_value(nums + [c], candidates, digits))
        return max_value


def arrange_nums(nums: list[int]) -> str:
    groups = [[nums[0], nums[1], nums[2]]]
    for i in range(1, len(nums) // 2 - 1):
        groups += [[nums[(start := i * 2) + 1], nums[start], nums[start + 2]]]
    groups += [[nums[-1], nums[-2], nums[1]]]
    min_index = groups.index(min(groups))
    return groups_to_str(groups[min_index:]) + groups_to_str(groups[:min_index])


def groups_to_str(nums: list[list[int]]) -> str:
    return ''.join(''.join(map(str, nums_sub)) for nums_sub in nums)


if __name__ == '__main__':
    main()
