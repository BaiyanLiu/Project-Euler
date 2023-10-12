import argparse
from functools import reduce
from operator import mul

import utils


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the value of the first triangle number to have over n divisors?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Lower limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    primes = utils.sieve(100)
    x, y = 0, 0
    while x <= args.n or reduce(mul, utils.num_factors(x, primes).values(), 1) <= args.n:
        x += (y := y + 1)
    print(x)


if __name__ == '__main__':
    main()
