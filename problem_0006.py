import argparse

import utils


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the difference between the sum of the squares of the first n natural numbers and the square '
                    'of the sum.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive).')
    return parser.parse_args()


def main():
    args = get_args()
    square_of_sum = utils.sum_series(args.n) ** 2
    sum_of_squares = sum(utils.square_nums(1, args.n + 1))
    print(square_of_sum - sum_of_squares)


if __name__ == '__main__':
    main()
