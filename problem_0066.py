"""
Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

https://projecteuler.net/problem=66
"""


import argparse
from itertools import count
from math import sqrt

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
    sqr_nums = utils.square_nums(2, 32)
    max_d, max_x = 0, 0
    for d in [i for i in range(2, args.n + 1) if i not in sqr_nums]:
        if (x := first_x(d)) > max_x:
            max_d, max_x = d, x
    print(max_d)


def first_x(d: int) -> int:
    """https://en.wikipedia.org/wiki/Pell's_equation"""
    a0 = int(sqrt(d))
    params, a = Params(0, 1, a0), [a0]
    for i in count(0):
        params = utils.continued_fraction_next_params(d, a0, params)
        a += [params.a]
        x, y = utils.continued_fraction_num_denom(0, i, a)
        if x ** 2 - d * y ** 2 == 1:
            return x


if __name__ == '__main__':
    main()
