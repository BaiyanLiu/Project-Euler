import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ '
                    'n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    values = set()
    for denom in range(5, args.n + 1):
        for num in range(denom // 3 + 1, denom // 2 + 1):
            values.add(num / denom)
    print(len(values) - 1)


if __name__ == '__main__':
    main()
