import concurrent.futures
from os import cpu_count

import utils


def main():
    nums = utils.sum_divisors(28123)
    abundants = sorted([i for i in nums.keys() if i < nums[i]])
    abundant_sums = set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = [executor.submit(sum_abundants, chunk, abundants) for chunk in utils.list_to_chunks(abundants)]
        for future in concurrent.futures.as_completed(futures):
            abundant_sums.update(future.result())
    print(utils.sum_series(28123) - sum(abundant_sums))


def sum_abundants(abundants_chunk: list[int], abundants: list[int]) -> set[int]:
    abundant_sums = set()
    for i in abundants_chunk:
        for j in abundants:
            if (k := i + j) > 28123 or j > i:
                break
            abundant_sums.add(k)
    return abundant_sums


if __name__ == '__main__':
    main()
