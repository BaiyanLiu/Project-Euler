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
