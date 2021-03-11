"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

https://projecteuler.net/problem=40
"""


from functools import reduce
from operator import mul


def main():
    indices = [10 ** i for i in range(7)]
    digit_groups = [1]
    for i in range(1, len(str(indices[-1]))):
        digit_groups.append(int(digit_groups[i - 1] + i * 9 * 10 ** (i - 1)))
    print(reduce(mul, [find_value(i, digit_groups) for i in indices]))


def find_value(index: int, digit_groups: list[int]) -> int:
    i = next(i for i in range(len(digit_groups) - 1, -1, -1) if index >= digit_groups[i])
    num = str(int(10 ** i + (offset := index - digit_groups[i]) / (i + 1)))
    return int(num[offset % (i + 1)])


if __name__ == '__main__':
    main()
