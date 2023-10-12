import argparse

from utils import is_palindrome


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the largest palindrome made from the product of two n-digit numbers.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of digits.')
    return parser.parse_args()


def main():
    args = get_args()
    max_num = 0
    for i in range(int(10 ** (args.n - 1)), limit := int(10 ** args.n)):
        for j in range(i, limit):
            if (num := i * j) > max_num and is_palindrome(str(num)):
                max_num = num
    print(max_num)


if __name__ == '__main__':
    main()
