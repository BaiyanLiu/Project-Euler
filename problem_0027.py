import math


def main():
    c = math.ceil(math.sqrt(1000 + 41))
    # Maximize (x - c) ^ 2 + (x - c) + 41
    while c ** 2 - c + 41 >= 1000:
        c -= 1
    a = -c * 2 + 1
    b = c ** 2 - c + 41
    print(a * b)


if __name__ == '__main__':
    main()
