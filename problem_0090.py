from itertools import combinations


rules = [(0, {1}), (0, {4}), (0, {6, 9}), (1, {6, 9}), (1, {8}), (2, {5}), (3, {6, 9}), (4, {6, 9})]


def main():
    num_valid = 0
    combos = list(combinations(range(10), 6))
    for cubes in ((set(i), set(j)) for i, j in combinations(combos, r=2)):
        if all(is_valid(cubes[0], cubes[1], rule) or is_valid(cubes[1], cubes[0], rule) for rule in rules):
            num_valid += 1
    print(num_valid)


def is_valid(cube_1: set[int], cube_2: set[int], rule: tuple[int, set[int]]) -> bool:
    return rule[0] in cube_1 and not rule[1].isdisjoint(cube_2)


if __name__ == '__main__':
    main()
