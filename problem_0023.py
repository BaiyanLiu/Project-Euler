"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

https://projecteuler.net/problem=23
"""


import concurrent.futures

import utils


def main():
    nums = utils.sum_divisors(28123)
    abundants = sorted([i for i in nums.keys() if i < nums[i]])
    abundant_sums = set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
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
