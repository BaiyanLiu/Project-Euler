from functools import reduce
from operator import mul


def main():
    indices = [10 ** i for i in range(7)]
    digit_groups = [1]
    for i in range(1, len(str(indices[-1]))):
        digit_groups.append(int(digit_groups[i - 1] + i * 9 * 10 ** (i - 1)))
    print(reduce(mul, [find_value(i, digit_groups) for i in indices]))


def find_value(index: int, digit_groups: list[int]) -> int:
    i = next(i for i in range(len(digit_groups) - 1, -1, -1) if index >= digit_groups[i])
    num = str(10 ** i + (offset := index - digit_groups[i]) // (i + 1))
    return int(num[offset % (i + 1)])


if __name__ == '__main__':
    main()
