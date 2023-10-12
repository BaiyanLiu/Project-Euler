from itertools import product


def main():
    print(max(sum(map(int, str(i ** j))) for i, j in product(range(2, 100), range(1, 100))))


if __name__ == '__main__':
    main()
