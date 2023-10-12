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
