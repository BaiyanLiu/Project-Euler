import argparse

from itertools import product


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many Sundays fell on the first of the month during 1 Jan 1901 to 31 Dec n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Year upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    sundays = 0
    day = 1
    for year, month in product(range(1901, args.n + 1), range(1, 13)):
        if (day := (day + num_days(month, year)) % 7) == 6:
            sundays += 1
    print(sundays)


def num_days(month: int, year: int) -> int:
    if month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 28 + (1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0)
    else:
        return 31


if __name__ == '__main__':
    main()
