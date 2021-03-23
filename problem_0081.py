"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right
and down, is indicated in bold red and is equal to 2427.

131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right
click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

https://projecteuler.net/problem=81
"""


from functools import lru_cache
from math import isqrt
from re import split
from sys import maxsize


matrix = list(map(int, split('[\\s,]', open('input/p081_matrix.txt').read().rstrip())))
width = isqrt(len(matrix))


def main():
    path, next_node = matrix[0], 0
    while next_node := find_next_node(next_node, 80)[0]:
        path += matrix[next_node]
        if next_node == len(matrix) - 1:
            print(path)


@lru_cache(maxsize=None)
def find_next_node(curr: int, depth: int) -> tuple[int, int]:
    min_node, min_value = 0, maxsize
    if curr % width != width - 1:
        if (value := look_ahead(curr + 1, depth)) < min_value:
            min_node, min_value = curr + 1, value
    if curr + width < len(matrix):
        if (value := look_ahead(curr + width, depth)) < min_value:
            min_node, min_value = curr + width, value
    return min_node, min_value


@lru_cache(maxsize=None)
def look_ahead(curr: int, depth: int) -> int:
    value = matrix[curr]
    if depth > 0 and curr != len(matrix) - 1:
        return value + find_next_node(curr, depth - 1)[1]
    return value


if __name__ == '__main__':
    main()
