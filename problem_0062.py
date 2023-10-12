import argparse


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the smallest cube for which exactly n permutations of its digits are cube.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of permutations')
    return parser.parse_args()


def main():
    args = get_args()
    perms = {}
    for i in range(2, 10000):
        if (k := ''.join(sorted(str(i ** 3)))) not in perms:
            perms[k] = []
        perms[k].append(i)
    print(next(v[0] ** 3 for v in perms.values() if len(v) == args.n))


if __name__ == '__main__':
    main()
