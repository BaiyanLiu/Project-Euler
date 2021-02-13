"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For
example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

https://projecteuler.net/problem=41
"""


import argparse

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='What is the largest n-digit pandigital prime that exists?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    primes = reversed(sieve(7654321))
    print(next(p for p in primes if is_pandigital(p)))


def is_pandigital(n: int) -> bool:
    n_len = len(n_str := str(n))
    return '0' not in n_str and n_len == len(set(n_str)) and max(n_str) == str(n_len)


if __name__ == '__main__':
    main()
