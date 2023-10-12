import argparse
from functools import lru_cache


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Which starting number, under n, produces the longest Collatz chain?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    print(max((nums := {i: collatz(i) for i in range(2, args.n)}), key=nums.get))


@lru_cache(maxsize=None)
def collatz(n: int) -> int:
    if n == 1:
        return 1
    return collatz(n // 2 if n % 2 == 0 else n * 3 + 1) + 1


if __name__ == '__main__':
    main()
