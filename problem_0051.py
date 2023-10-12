import argparse

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) '
                    'with the same digit, is part of an n prime value family.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of primes')
    return parser.parse_args()


def main():
    args = get_args()
    primes = sieve(1000000)
    for max_digits in range(2, 7):
        lower, upper = 10 ** (max_digits - 1), 10 ** max_digits
        primes_sub = [p for p in primes if lower < p < upper]
        if group_start := find_group_start_all(-1, [], max_digits, primes_sub, args.n):
            print(group_start)
            break


def find_group_start_all(curr: int, digits: list[int], max_digits, primes: list[int], n: int) -> int:
    for digit in range(curr + 1, max_digits):
        if next_prime := find_group_start(digits + [digit], max_digits, primes, n):
            return next_prime


def find_group_start(digits: list[int], max_digits: int, primes: list[int], n: int) -> int:
    for i in map(str, range(10)):
        curr = digits[-1]
        if len(primes_sub := [p for p in primes if str(p)[curr] == i]) >= n:
            if len(group := [p for p in primes_sub if has_same_digits(p, digits)]) == n:
                return group[0]
            elif group_start := find_group_start_all(curr, digits, max_digits, primes_sub, n):
                return group_start


def has_same_digits(n: int, ignored: list[int]) -> bool:
    n_str = str(n)
    return len({n_str[i] for i in range(len(n_str)) if i not in ignored}) == 1


if __name__ == '__main__':
    main()
