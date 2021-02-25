"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and
twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

https://projecteuler.net/problem=46
"""


import argparse
import utils


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='What is the smallest odd composite that cannot be written as the sum of a prime and twice a '
                    'square?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    primes = utils.sieve(10000)
    squares = {i ** 2 * 2 for i in range(1, 100)}
    divisors = utils.sum_divisors(10000)
    nums = [i for i in range(1, 10000, 2) if i in divisors]
    print(next(i for i in nums if all(i - prime not in squares for prime in primes if prime < i)))


if __name__ == '__main__':
    main()
