"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal
expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
for all the irrational square roots.

https://projecteuler.net/problem=80
"""


import math


def main():
    print(sum(map(sum_digits, range(1, 101))))


def sum_digits(n: int) -> int:
    n_sqrt = math.sqrt(n)
    if int(n_sqrt) == n_sqrt:
        return 0
    value = math.isqrt(n * 10 ** 198)
    return sum(map(int, str(value)))


if __name__ == '__main__':
    main()
