"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

https://projecteuler.net/problem=52
"""


from itertools import count

from utils import is_permutation


def main():
    print(next(i for i in count(1) if all(is_permutation(i * j, i) for j in range(2, 7))))


if __name__ == '__main__':
    main()
