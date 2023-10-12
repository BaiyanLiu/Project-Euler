from itertools import count

from utils import num_partitions


def main():
    print(next(i for i in count(24, 25) if num_partitions(i) % 1000000 == 0))


if __name__ == '__main__':
    main()
