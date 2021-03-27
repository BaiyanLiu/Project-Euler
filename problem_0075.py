"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle
in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right
angle triangle be formed?

https://projecteuler.net/problem=75
"""


import argparse

from utils import pythagorean_triples


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Given that L is the length of the wire, for how many values of L ≤ n can exactly one integer '
                    'sided right angle triangle be formed?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    """https://en.wikipedia.org/wiki/Pythagorean_triple"""
    args = get_args()
    triples = {}
    for a, b, c in pythagorean_triples(args.n):
        if (p := a + b + c) not in triples:
            triples[p] = set()
        triples[p].add(a)
    print(sum(1 for i in triples.values() if len(i) == 1))


if __name__ == '__main__':
    main()
