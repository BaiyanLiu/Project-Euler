import argparse
from itertools import count
from math import isqrt

import utils
from utils import ContinuedFractionParams as Params


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the value of D ≤ n in minimal solutions of x for which the largest value of x is obtained.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    sqr_nums = utils.square_nums(2, isqrt(args.n) + 1)
    max_d, max_x = 0, 0
    for d in [i for i in range(2, args.n + 1) if i not in sqr_nums]:
        if (x := first_x(d)) > max_x:
            max_d, max_x = d, x
    print(max_d)


def first_x(d: int) -> int:
    """https://en.wikipedia.org/wiki/Pell's_equation"""
    a0 = isqrt(d)
    params, a = Params(0, 1, a0), [a0]
    for i in count(0):
        params = utils.continued_fraction_next_params(d, a0, params)
        a += [params.a]
        x, y = utils.continued_fraction_num_denom(0, i, a)
        if x ** 2 - d * y ** 2 == 1:
            return x


if __name__ == '__main__':
    main()
