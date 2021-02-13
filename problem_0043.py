"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

https://projecteuler.net/problem=43
"""


import argparse

from itertools import product


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='Find the sum of all 0 to 9 pandigital numbers with this property.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    rules = {(1, 2, 3): 2, (2, 3, 4): 3, (3, 4, 5): 5, (4, 5, 6): 7,
             (5, 6, 7): 11, (6, 7, 8): 13, (7, 8, 9): 17}
    sums = 0
    for num in generate_numbers():
        num_str = str(num)
        if all(int(''.join([num_str[i] for i in j])) % rules[j] == 0 for j in rules):
            sums += num
    print(sums)


def generate_numbers() -> list[int]:
    nums = []
    # [1-9]\\d{2}[02468]\\d[05]\\d{4}
    for d1, d2, d3, d4, d5, d6, d7, d8, d9 in product(range(7), range(6), range(5), [0, 5], range(4),
                                                      range(0, 9, 2), range(3), range(2), range(1, 10)):
        if d6 == d4 or d9 == d4 or d9 == d6:
            continue
        remaining = [i for i in range(10) if i != d4 and i != d6 and i != d9]
        d1, d2, d3, d5, d7, d8 = map(remaining.pop, [d1, d2, d3, d5, d7, d8])
        d0 = remaining[0]
        digits = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
        nums.append(sum(digits[i] * 10 ** i for i in range(10)))
    return nums


if __name__ == '__main__':
    main()
