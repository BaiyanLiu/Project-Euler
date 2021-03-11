"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

https://projecteuler.net/problem=52
"""


def main():
    print(next(i for i in range(1, 200000) if all(sorted(str(i * j)) == sorted(str(i)) for j in range(2, 7))))


if __name__ == '__main__':
    main()
