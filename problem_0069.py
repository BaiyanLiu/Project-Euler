import argparse

from utils import totients


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the value of n ≤ a for which n/φ(n) is a maximum.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('a', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    print(max(values := {n: n / phi for n, phi in totients(args.a).items()}, key=values.get))


if __name__ == '__main__':
    main()
