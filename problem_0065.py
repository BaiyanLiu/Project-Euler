"""
The square root of 2 can be written as an infinite continued fraction.
sqrt(2) = 1 + 1 / (2 + (1 / (2 + 1 / (2 + 1 / (2 + ...))))

The infinite continued fraction can be written, sqrt(2) = [1; (2)], (2) indicates that 2 repeats ad infinitum. In a
similar way, sqrt(23) = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational
approximations. Let us consider the convergents for sqrt(2)
1 + 1 / 2
= 3 / 2 * 1 + 1 / (2 + 1 / 2))
= 7 / 5 * 1 + 1 / (2 + 1 / (2 + 1 / 2)))
= 17 / 12 * 1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / 2))))
= 41 / 29.

Hence the sequence of the first ten convergents for sqrt(2) are:
1, 3 / 2, 7 / 5, 17 / 12, 41 / 29, 99 / 70, 239 / 169, 577 / 408, 1393 / 985, 3363 / 2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8 / 3, 11 / 4, 19 / 7, 87 / 32, 106 / 39, 193 / 71, 1264 / 465, 1457 / 536, ...

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

https://projecteuler.net/problem=65
"""


import argparse

from utils import continued_fraction_num_denom


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the sum of digits in the numerator of the nth convergent of the continued fraction for e.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The convergent')
    return parser.parse_args()


def main():
    args = get_args()
    a = list(map(get_a, range(args.n)))
    print(sum(map(int, str(continued_fraction_num_denom(0, args.n - 1, a)[0]))))


def get_a(n: int) -> int:
    if n == 0:
        return 2
    elif n % 3 == 2:
        return (n // 3 + 1) * 2
    else:
        return 1


if __name__ == '__main__':
    main()
