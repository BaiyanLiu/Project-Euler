import math


def main():
    print(sum(map(sum_digits, range(1, 101))))


def sum_digits(n: int) -> int:
    n_sqrt = math.sqrt(n)
    if int(n_sqrt) == n_sqrt:
        return 0
    value = math.isqrt(n * 10 ** 198)
    return sum(map(int, str(value)))


if __name__ == '__main__':
    main()
