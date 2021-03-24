"""
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell
in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing an 80 by 80 matrix.

https://projecteuler.net/problem=82
"""


from functools import lru_cache
from math import isqrt
from re import split
from sys import maxsize


matrix = list(map(int, split('[\\s,]', open('input/p082_matrix.txt').read().rstrip())))
width = isqrt(len(matrix))


def main():
    print(min(map(find_min_path, range(0, len(matrix), width))))


def find_min_path(curr: int) -> int:
    path, curr = matrix[curr] + matrix[curr + 1], curr + 1
    prev, next_node = 0, 0
    while (next_node := find_next_node(curr, prev, 110)[0]) and (prev := curr) and (curr := next_node):
        path += matrix[next_node]
        if at_end(next_node):
            return path


def find_next_node(curr: int, prev, depth: int) -> tuple[int, int]:
    min_node, min_value = 0, maxsize
    if (right := curr + 1) % width != 0:
        if (value := look_ahead(right, curr, depth)) < min_value:
            min_node, min_value = right, value
    if (up := curr - width) > 0 and up != prev:
        if (value := look_ahead(up, curr, depth)) < min_value:
            min_node, min_value = up, value
    if (down := curr + width) < len(matrix) and down != prev:
        if (value := look_ahead(down, curr, depth)) < min_value:
            min_node, min_value = down, value
    return min_node, min_value


@lru_cache(maxsize=None)
def look_ahead(curr: int, prev: int, depth: int) -> int:
    value = matrix[curr]
    if depth > 0 and not at_end(curr):
        return value + find_next_node(curr, prev, depth - 1)[1]
    return value


def at_end(node: int) -> bool:
    return node % width == width - 1


if __name__ == '__main__':
    main()
