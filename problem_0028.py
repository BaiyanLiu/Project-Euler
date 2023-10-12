import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the sum of the numbers on the diagonals in a n by n spiral formed in the same way?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Size')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum([(i ** 2 + (i - 2) ** 2 + i - 1) * 2 for i in range(args.n, 1, -2)]) + 1)


if __name__ == '__main__':
    main()
