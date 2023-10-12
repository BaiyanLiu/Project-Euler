import argparse

from utils import num_partitions


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many different ways can n be written as a sum of at least two positive integers?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='The number')
    return parser.parse_args()


def main():
    args = get_args()
    print(num_partitions(args.n) - 1)


if __name__ == '__main__':
    main()
