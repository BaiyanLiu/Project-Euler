from itertools import product


def main():
    prod = 1
    for i, j in product(range(1, 10), range(1, 10)):
        if i == j:
            continue
        frac = i / j
        if any([(i * 10 + k) / (j + k * 10) == frac for k in range(1, 10)]):
            prod *= frac
    print(round(1 / prod))


if __name__ == '__main__':
    main()
