import concurrent.futures
from os import cpu_count
from sys import maxsize

import utils


def main():
    nums = sorted(nums_set := utils.pentagonal_nums(1, 10000))
    min_num = maxsize
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = [executor.submit(find_min_num, chunk, nums, nums_set) for chunk in utils.list_to_chunks(nums)]
        for future in concurrent.futures.as_completed(futures):
            min_num = min(min_num, future.result())
    print(min_num)


def find_min_num(nums_chunk: list[int], nums: list[int], nums_set: set[int]) -> int:
    min_num = maxsize
    for i in nums_chunk:
        for j in nums:
            if j > i:
                break
            if i + j in nums_set and i - j in nums_set:
                min_num = min(min_num, i - j)
    return min_num


if __name__ == '__main__':
    main()
