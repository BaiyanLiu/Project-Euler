from itertools import count

from utils import is_permutation


def main():
    print(next(i for i in count(1) if all(is_permutation(i * j, i) for j in range(2, 7))))


if __name__ == '__main__':
    main()
