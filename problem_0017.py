import argparse


ZERO_TO_NINETEEN = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
TWENTY_TO_NINETY = [6, 6, 5, 5, 5, 7, 6, 6]


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='If all the numbers from 1 to n inclusive were written out in words, how many letters would be '
                    'used?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    print(sum(map(num_chars, range(1, args.n + 1))))


def num_chars(n: int) -> int:
    chars = ZERO_TO_NINETEEN[thousands] + 8 if (thousands := n // 1000) > 0 else 0
    chars += ZERO_TO_NINETEEN[hundreds] + 7 if (hundreds := n % 1000 // 100) > 0 else 0
    tens = n % 100 // 10
    ones = n % 10
    if tens > 0 or ones > 0:
        if chars > 0:
            chars += 3
        if tens < 2:
            chars += ZERO_TO_NINETEEN[tens * 10 + ones]
        else:
            chars += TWENTY_TO_NINETY[tens - 2] + ZERO_TO_NINETEEN[ones]
    return chars


if __name__ == '__main__':
    main()
