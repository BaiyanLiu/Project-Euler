"""
All square roots are periodic when written as continued fractions and can be written in the form:
sqrt(N) = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + ...)))

For example, let us consider sqrt(23):
sqrt(23) = 4 + sqrt(23) - 4 = 4 + 1 / (1 / (sqrt(23) - 4)) = 4 + 1 / (1 + (sqrt(23) - 3) /  7)

If we continue we would get the following expansion:
sqrt(23) = 4 + 1 / (1 + 1  / (3 + 1 / (1 + 1 / (8 + ...)))

The process can be summarised as follows:
a0 = 4, 1 / (sqrt(23) - 4) = (sqrt(23) + 4) / 7 = 1 + (sqrt(23) - 3) / 7
...

It can be seen that the sequence is repeating. For conciseness, we use the notation sqrt(23) = [4;(1,3,1,8)], 
to indicate that the block (1,3,1,8) repeats indefinitely. 

The first ten continued fraction representations of (irrational) square roots are:

sqrt(2) = [1;(2)], period=1
sqrt(3) = [1;(1,2)], period=2
sqrt(5) = [2;(4)], period=1
sqrt(6) = [2;(2,4)], period=2
sqrt(7) = [2;(1,1,1,4)], period=4
sqrt(8) = [2;(1,4)], period=2
sqrt(10) = [3;(6)], period=1
sqrt(11) = [3;(3,6)], period=2
sqrt(12) = [3;(2,6)], period=2
sqrt(13) = [3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?

https://projecteuler.net/problem=64
"""


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
