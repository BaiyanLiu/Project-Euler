"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

https://projecteuler.net/problem=34
"""


import concurrent.futures

import utils


def main():
    factorials = utils.factorial_series(9)
    factorials = {str(i): factorials[i] for i in range(len(factorials))}
    i, max_num = 9, factorials['9']
    while (i := i * 10 + 9) < (max_num := max_num + factorials['9']):
        pass
    nums = list(range(10, max_num))
    nums_sum = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(sum_nums, chunk, factorials) for chunk in utils.list_to_chunks(nums)]
        for future in concurrent.futures.as_completed(futures):
            nums_sum += future.result()
    print(nums_sum)


def sum_nums(nums: list[int], factorials: dict[str, int]) -> int:
    return sum([i for i in nums if sum([factorials[j] for j in str(i)]) == i])


if __name__ == '__main__':
    main()
