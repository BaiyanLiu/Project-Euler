"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

https://projecteuler.net/problem=50
"""


import argparse

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Which prime, below n, can be written as the sum of the most consecutive primes?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    primes = sieve(args.n - 1)
    num_primes, primes_set = len(primes), set(primes)
    max_len, max_sum = 0, 0
    for i in primes:
        if max_len > 0 and i > args.n // max_len:
            break
        curr_len, curr_sum = 1, i
        for j in [p for p in primes if p > i]:
            if (curr_sum := curr_sum + j) >= args.n:
                break
            if (curr_len := curr_len + 1) > max_len and curr_sum in primes_set:
                max_len, max_sum = curr_len, curr_sum
    print(max_sum)


if __name__ == '__main__':
    main()
