"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5 3) = 10

In general, (n r) = n! / r!(n-r)!, where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: (23 10) = 1144066.

How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?

https://projecteuler.net/problem=53
"""


from utils import factorial_series


def main():
    nums = factorial_series(100)
    print(sum(1 for i in range(23, 101) for j in range(i + 1) if nums[i] // (nums[j] * nums[i - j]) > 1000000))


if __name__ == '__main__':
    main()
