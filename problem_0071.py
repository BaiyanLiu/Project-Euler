"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of
the fraction immediately to the left of 3/7.

https://projecteuler.net/problem=71
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='By listing the set of reduced proper fractions for d ≤ n in ascending order of size, find the '
                    'numerator of the fraction immediately to the left of 3/7.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    fractions = {}
    for denom in range(2, args.n + 1):
        num_floor = int(num := denom * 3 / 7)
        if num_floor != num and num_floor not in fractions:
            fractions[num_floor] = denom
    print(max(values := {k: k / v for k, v in fractions.items()}, key=values.get))


if __name__ == '__main__':
    main()
