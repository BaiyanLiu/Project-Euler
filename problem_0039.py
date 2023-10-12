from math import sqrt


def main():
    solutions = {}
    for a in range(1, 996):
        for b in range(a + 1, 998):
            if (c := sqrt(a ** 2 + b ** 2)) == int(c):
                if (p := int(a + b + c)) > 1000:
                    break
                solutions[p] = solutions.get(p, 0) + 1
    print(max(solutions, key=solutions.get))


if __name__ == '__main__':
    main()
