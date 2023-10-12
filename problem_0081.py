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
        if at_end(next_node):
            print(path)
            break


def find_next_node(curr: int, depth: int) -> tuple[int, int]:
    min_node, min_value = 0, maxsize
    if (right := curr + 1) % width != 0:
        if (value := look_ahead(right, depth)) < min_value:
            min_node, min_value = right, value
    if (down := curr + width) < len(matrix):
        if (value := look_ahead(down, depth)) < min_value:
            min_node, min_value = down, value
    return min_node, min_value


@lru_cache(maxsize=None)
def look_ahead(curr: int, depth: int) -> int:
    value = matrix[curr]
    if depth > 0 and not at_end(curr):
        value += find_next_node(curr, depth - 1)[1]
    return value


def at_end(node: int) -> bool:
    return node == len(matrix) - 1


if __name__ == '__main__':
    main()
