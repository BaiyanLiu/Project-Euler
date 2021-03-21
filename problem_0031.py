"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

https://projecteuler.net/problem=31
"""


import argparse
from functools import lru_cache


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many different ways can £n be made using any number of coins?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Pounds')
    return parser.parse_args()


def main():
    args = get_args()
    print(num_combos(args.n * 100, values := (200, 100, 50, 20, 10, 5, 2, 1), values[0]))


@lru_cache(maxsize=None)
def num_combos(n: int, values: tuple, prev_value: int) -> int:
    if n == 0:
        return 1
    else:
        combos = 0
        for i in values:
            if i <= n and i <= prev_value:
                combos += num_combos(n - i, values, i)
        return combos


if __name__ == '__main__':
    main()
