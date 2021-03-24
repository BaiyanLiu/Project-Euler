"""
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell
in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

131     673     (234)   (103)   (18)
(201)   (96)    (342)   965     150
630     803     746     422     111
537     699     497     121     956
805     732     524     37      331

Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing an 80 by 80 matrix.

https://projecteuler.net/problem=82
"""


from math import isqrt
from re import split
from sys import maxsize

from utils import matrix_neighbors


def main():
    matrix = list(map(int, split('[\\s,]', open('input/p082_matrix.txt').read().rstrip())))
    width = isqrt(len(matrix))
    print(min(v for k, v in dijkstra(matrix, width).items() if k % width == width - 1))


def dijkstra(matrix: list[int], width: int) -> dict[int, int]:
    """https://en.wikipedia.org/wiki/Dijkstra's_algorithm"""
    dist = dict.fromkeys(range(len(matrix)), maxsize)
    for i in range(0, len(matrix), width):
        dist[i] = matrix[i]
    queue = dist.copy()

    while len(queue) > 0:
        queue.pop(curr := min(queue, key=queue.get))
        for neighbor in matrix_neighbors(curr, matrix, width):
            if neighbor not in queue:
                continue
            if (alt_dist := dist[curr] + matrix[neighbor]) < dist[neighbor]:
                queue[neighbor] = dist[neighbor] = alt_dist
    return dist


if __name__ == '__main__':
    main()
