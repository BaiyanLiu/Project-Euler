"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one
followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

https://projecteuler.net/problem=56
"""


from itertools import product


def main():
    print(max(sum(map(int, str(i ** j))) for i, j in product(range(2, 100), range(1, 100))))


if __name__ == '__main__':
    main()
