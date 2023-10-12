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
