import argparse
import concurrent.futures
import itertools
import math
from os import cpu_count

import utils


origin = (0, 0)


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Given that 0 <= x1, y1, x2, y2 <= n, how many right triangles can be formed?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    nums = range(0, args.n + 1)
    pairs = itertools.combinations([point for point in itertools.product(nums, nums) if point != origin], 2)
    triangles = [pair + (origin,) for pair in pairs]

    right_triangles = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = [executor.submit(count_right_triangles, chunk) for chunk in utils.list_to_chunks(triangles)]
        for future in concurrent.futures.as_completed(futures):
            right_triangles += future.result()
    print(right_triangles)


def count_right_triangles(triangles: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]) -> int:
    right_triangles = 0
    for (a, b, c) in triangles:
        d = [math.dist(a, b), math.dist(b, c), math.dist(c, a)]
        if is_right_angle(d[0], d[1], d[2]) or is_right_angle(d[1], d[2], d[0]) or is_right_angle(d[2], d[0], d[1]):
            right_triangles += 1
    return right_triangles


def is_right_angle(da: float, db: float, dc: float) -> bool:
    return abs((pow(da, 2) + pow(db, 2) - pow(dc, 2)) / (2 * da * db)) < 1e-6


if __name__ == '__main__':
    main()
