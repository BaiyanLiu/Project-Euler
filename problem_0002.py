import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of '
                    'the even-valued terms.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive).')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum_even_fib(1, 1, args.n))


def sum_even_fib(a: int, b: int, n: int) -> int:
    if (c := a + b) > n:
        return 0
    return (c if c % 2 == 0 else 0) + sum_even_fib(b, c, n)


if __name__ == '__main__':
    main()
