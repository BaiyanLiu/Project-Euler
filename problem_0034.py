"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

https://projecteuler.net/problem=34
"""


import argparse

from utils import factorial_series


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='Find the sum of all numbers which are equal to the sum of the factorial of their digits.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    factorials = factorial_series(9)
    factorials = {str(i): factorials[i] for i in range(len(factorials))}
    i, max_num = 9, factorials['9']
    while (i := i * 10 + 9) < (max_num := max_num + factorials['9']):
        pass
    print(sum([i for i in range(10, max_num) if sum([factorials[j] for j in str(i)]) == i]))


if __name__ == '__main__':
    main()
