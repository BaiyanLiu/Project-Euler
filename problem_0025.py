import argparse
import math


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='What is the index of the first term in the Fibonacci sequence to contain n digits?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of digits')
    return parser.parse_args()


def main():
    args = get_args()
    phi = (1 + math.sqrt(5)) / 2
    # 10 ^ (n - 1) < phi ^ n / sqrt(5)
    print(math.ceil((math.log10(10) * (args.n - 1) + math.log10(5) / 2) / math.log10(phi)))


if __name__ == '__main__':
    main()
