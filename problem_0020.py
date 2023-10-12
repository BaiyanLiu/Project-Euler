import argparse

from math import factorial


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the sum of the digits in the number n!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The number')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum(map(int, str(factorial(args.n)))))


if __name__ == '__main__':
    main()
