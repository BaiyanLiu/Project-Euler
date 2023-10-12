import argparse

from utils import continued_fraction_num_denom


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the sum of digits in the numerator of the nth convergent of the continued fraction for e.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The convergent')
    return parser.parse_args()


def main():
    args = get_args()
    a = list(map(get_a, range(args.n)))
    print(sum(map(int, str(continued_fraction_num_denom(0, args.n - 1, a)[0]))))


def get_a(n: int) -> int:
    if n == 0:
        return 2
    elif n % 3 == 2:
        return (n // 3 + 1) * 2
    else:
        return 1


if __name__ == '__main__':
    main()
