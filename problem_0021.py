import argparse

from utils import sum_divisors


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Evaluate the sum of all the amicable numbers under n.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    sums = sum_divisors(args.n)
    print(sum([i for i in sums if sums[i] != i and sums[i] in sums and sums[sums[i]] == i]))


if __name__ == '__main__':
    main()
