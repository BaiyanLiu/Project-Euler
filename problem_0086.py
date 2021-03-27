"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is
shown on the diagram.
p086.png

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always
have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions,
up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least
value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.

https://projecteuler.net/problem=86
"""


import argparse

from utils import pythagorean_triples


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the least value of M such that the number of solutions first exceeds n',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Minimum number of solutions (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    triples = {}
    for a, b, c in set(pythagorean_triples(10000)):
        if a * 2 >= b:
            triples[a] = triples.get(a, 0) + (a - (b - a)) // 2 + 1
        triples[b] = triples.get(b, 0) + a // 2
    num_solutions, i = 0, 0
    for i in sorted(triples):
        if (num_solutions := num_solutions + triples[i]) > args.n:
            break
    print(i)


if __name__ == '__main__':
    main()
