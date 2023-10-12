import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the sum of all the multiples of a or b below n.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('a', type=int, help='First number.')
    parser.add_argument('b', type=int, help='Second number.')
    parser.add_argument('n', type=int, help='Upper limit (exclusive).')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum(multiples(args.a, args.n) | multiples(args.b, args.n)))


def multiples(x: int, n: int) -> set[int]:
    return set(range(x, n, x))


if __name__ == '__main__':
    main()
