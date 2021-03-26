"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
p085.png

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid
with the nearest solution.

https://projecteuler.net/problem=85
"""


from itertools import count
from math import isqrt
from sys import maxsize


def main():
    min_delta, min_area = maxsize, 0
    for w in count(2):
        w_value = w * (w + 1)
        if (h := isqrt(8000000 // w_value)) < 2:
            break
        if (delta := abs(h * (h + 1) * w_value / 4 - 2000000)) < min_delta:
            min_delta, min_area = delta, w * h
    print(min_area)


if __name__ == '__main__':
    main()
