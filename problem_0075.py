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
from itertools import count


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
    triangles = {}
    for m in count(2):
        if (m2 := m ** 2) * 2 + m * 2 > args.n:
            break
        for n in range(1, m):
            if m2 * 2 + m * n * 2 > args.n:
                break
            a, b, c = sorted([m2 - (n2 := n ** 2), m * n * 2, m2 + n2])
            p = a + b + c
            k = 0
            while (pk := p * (k := k + 1)) <= args.n:
                if pk not in triangles:
                    triangles[pk] = set()
                triangles[pk].add(a * k)
    print(sum(1 for i in triangles.values() if len(i) == 1))


if __name__ == '__main__':
    main()
