import argparse
import math


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the largest prime factor of n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The number.')
    return parser.parse_args()


def main():
    args = get_args()
    print(fermat(args.n))


def fermat(n: int) -> int:
    """https://en.wikipedia.org/wiki/Fermat's_factorization_method"""
    a = math.ceil(math.sqrt(n))
    while (b := math.sqrt(a ** 2 - n)) != int(b):
        a += 1
    if a - b == n or a + b == n:
        return n
    else:
        return max(fermat(int(a - b)), fermat(int(a + b)))


if __name__ == '__main__':
    main()
