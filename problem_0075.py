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
