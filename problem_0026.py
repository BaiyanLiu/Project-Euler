import argparse

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the value of d < n for which 1/d contains the longest recurring cycle in its decimal '
                    'fraction part.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    max_cycle, max_num = 0, 0
    for num in sieve(args.n):
        cycle, digit, first_digit = 0, 1, None
        while (cycle := cycle + 1) and (digit := digit % num * 10):
            if first_digit is None:
                first_digit = digit
                continue
            elif first_digit != digit:
                continue
            if cycle > max_cycle:
                max_cycle, max_num = cycle, num
            break
    print(max_num)


if __name__ == '__main__':
    main()
