import utils


def main():
    tri_nums = utils.triangle_nums(45, 141)
    sqr_nums = utils.square_nums(32, 100)
    pen_nums = utils.pentagonal_nums(26, 82)
    hex_nums = utils.hexagonal_nums(23, 71)
    hep_nums = {i * (5 * i - 3) // 2 for i in range(21, 64)}
    oct_nums = {i * (3 * i - 2) for i in range(19, 59)}
    all_seqs = [tri_nums, sqr_nums, pen_nums, hex_nums, hep_nums, oct_nums]
    print(next(group_sum for i in tri_nums if (group_sum := find_group_sum({0}, [i], all_seqs))))


def find_group_sum(seqs: set[int], nums: list[int], all_seqs: list[set[int]]) -> int:
    curr_num = nums[-1]
    curr_suffix = curr_num % 100
    if len(nums) == 6:
        return sum(nums) if nums[0] // 100 == curr_suffix else None
    for seq in [i for i in range(len(all_seqs)) if i not in seqs]:
        for num in [i for i in all_seqs[seq] if i // 100 == curr_suffix]:
            if group_sum := find_group_sum(seqs | {seq}, nums + [num], all_seqs):
                return group_sum


if __name__ == '__main__':
    main()
