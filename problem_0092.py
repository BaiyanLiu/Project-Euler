import argparse
import concurrent.futures
import sys
from functools import lru_cache
from os import cpu_count

import utils


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many starting numbers below n will arrive at 89?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    sys.setrecursionlimit(args.n)
    num_valid = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = [executor.submit(count_valid, chunk) for chunk in utils.list_to_chunks(list(range(args.n - 1, 0, -1)))]
        for future in concurrent.futures.as_completed(futures):
            num_valid += future.result()
    print(num_valid)


def count_valid(nums: list[int]) -> int:
    return sum(1 for i in nums if is_valid(i))


@lru_cache(maxsize=None)
def is_valid(num: int) -> bool:
    if (next_num := sum(pow(int(digit), 2) for digit in str(num))) == 89:
        return True
    elif next_num == 1:
        return False
    else:
        return is_valid(next_num)


if __name__ == '__main__':
    main()
