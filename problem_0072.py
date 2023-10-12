import argparse

from utils import totients


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many elements would be contained in the set of reduced proper fractions for d ≤ n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum(totients(args.n).values()))


if __name__ == '__main__':
    main()
