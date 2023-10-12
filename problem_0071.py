import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='By listing the set of reduced proper fractions for d ≤ n in ascending order of size, find the '
                    'numerator of the fraction immediately to the left of 3/7.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (inclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    fractions = {}
    for denom in range(5, args.n + 1):
        num_floor = int(num := denom * 3 / 7)
        if num_floor != num and num_floor not in fractions:
            fractions[num_floor] = denom
    print(max(values := {k: k / v for k, v in fractions.items()}, key=values.get))


if __name__ == '__main__':
    main()
