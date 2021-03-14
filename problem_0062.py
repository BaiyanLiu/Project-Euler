"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

https://projecteuler.net/problem=62
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the smallest cube for which exactly n permutations of its digits are cube.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of permutations')
    return parser.parse_args()


def main():
    args = get_args()
    perms = {}
    for i in range(2, 10000):
        perms[k] = perms.get(k := ''.join(sorted(str(i ** 3))), []) + [i]
    print(next(v[0] ** 3 for v in perms.values() if len(v) == args.n))


if __name__ == '__main__':
    main()
