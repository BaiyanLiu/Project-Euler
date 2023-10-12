import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + n^n.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    sums, limit = 0, 10 ** 10
    for i in range(1, args.n + 1):
        i_sum = 1
        for unused in range(i):
            i_sum = (i_sum * i) % limit
        sums = sums + i_sum
    print(f'{sums % limit:010}')


if __name__ == '__main__':
    main()
