"""
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up,
and down, is indicated in bold red and is equal to 2297.

131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt (
right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

https://projecteuler.net/problem=83
"""


from math import isqrt
from re import split
from sys import maxsize

from utils import matrix_neighbors


def main():
    matrix = list(map(int, split('[\\s,]', open('input/p081_matrix.txt').read().rstrip())))
    print(a_star(matrix))


def a_star(matrix: list[int]) -> int:
    """https://en.wikipedia.org/wiki/A*_search_algorithm"""
    width = isqrt(len(matrix))
    dist = dict.fromkeys(range(len(matrix)), maxsize)
    score = dist.copy()
    dist[0], score[0] = matrix[0], heuristic(0, width)
    queue = score.copy()

    while len(queue) > 0:
        if (curr := min(queue, key=queue.get)) == len(matrix) - 1:
            return dist[curr]
        queue.pop(curr)
        for neighbor in matrix_neighbors(curr, matrix, width, True):
            if (alt_dist := dist[curr] + matrix[neighbor]) < dist[neighbor]:
                dist[neighbor] = alt_dist
                queue[neighbor] = score[neighbor] = alt_dist + heuristic(neighbor, width)


def heuristic(node: int, width: int) -> int:
    return width - (node // width) + width - (node % width)


if __name__ == '__main__':
    main()
