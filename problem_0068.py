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
