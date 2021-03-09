"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43,
53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having
seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773,
and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.

https://projecteuler.net/problem=51
"""


import argparse

from utils import sieve


NUMS = list(map(str, range(10)))


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) '
                    'with the same digit, is part of an n prime value family. ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The number of primes')
    return parser.parse_args()


def main():
    args = get_args()
    primes = sieve(1000000)
    for max_digits in range(2, 7):
        lower_lim, upper_lim = 10 ** (max_digits - 1), 10 ** max_digits
        primes_sub = [prime for prime in primes if lower_lim < prime < upper_lim]
        if group_start := find_group_start_all(-1, [], max_digits, primes_sub, args.n):
            print(group_start)
            break


def find_group_start_all(curr_digit: int, digits: list[int], max_digits, primes: list[int], n: int) -> int:
    for digit in range(curr_digit + 1, max_digits):
        if next_prime := find_group_start(digits + [digit], max_digits, primes, n):
            return next_prime


def find_group_start(digits: list[int], max_digits: int, primes: list[int], n: int) -> int:
    for i in NUMS:
        curr_digit = digits[-1]
        primes_sub = [prime for prime in primes if str(prime)[curr_digit] == i]
        if len(primes_sub) >= n:
            if len(group := [prime for prime in primes_sub if has_same_digits(prime, digits)]) == n:
                return group[0]
            elif group_start := find_group_start_all(curr_digit, digits, max_digits, primes_sub, n):
                return group_start


def has_same_digits(n: int, ignored_digits: list[int]) -> bool:
    n_str = str(n)
    return len({n_str[i] for i in range(len(n_str)) if i not in ignored_digits}) == 1


if __name__ == '__main__':
    main()
