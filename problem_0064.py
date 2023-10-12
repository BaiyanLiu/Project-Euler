import argparse
from math import isqrt

import utils
from utils import ContinuedFractionParams as Params


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many continued fractions for N <= n have an odd period?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum(1 for i in range(2, args.n + 1) if len_cycle(i, a0 := isqrt(i), [Params(0, 1, a0)]) % 2 != 0))


def len_cycle(i: int, a0: int, params: list[Params]) -> int:
    if not (curr := utils.continued_fraction_next_params(i, a0, params[-1])):
        return 0
    elif curr in params:
        return len(params) - 1
    else:
        return len_cycle(i, a0, params + [curr])


if __name__ == '__main__':
    main()
