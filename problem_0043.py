import concurrent.futures
from itertools import product
from os import cpu_count


def main():
    rules = {(1, 2, 3): 2, (2, 3, 4): 3, (3, 4, 5): 5, (4, 5, 6): 7,
             (5, 6, 7): 11, (6, 7, 8): 13, (7, 8, 9): 17}
    nums_sum = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = [executor.submit(generate_and_sum, i, rules) for i in range(6)]
        for future in concurrent.futures.as_completed(futures):
            nums_sum += future.result()
    print(nums_sum)


def generate_and_sum(n: int, rules: dict[(int, int, int), int]) -> int:
    nums = []
    # [1-9]\\d{2}[02468]\\d[05]\\d{4}
    for d1, d2, d3, d4, d5, d6, d7, d8, d9 in product(range(7), [n], range(5), [0, 5], range(4),
                                                      range(0, 9, 2), range(3), range(2), range(1, 10)):
        if d6 == d4 or d9 == d4 or d9 == d6:
            continue
        remaining = [i for i in range(10) if i != d4 and i != d6 and i != d9]
        d1, d2, d3, d5, d7, d8 = map(remaining.pop, [d1, d2, d3, d5, d7, d8])
        d0 = remaining[0]
        digits = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
        nums.append(sum(digits[i] * 10 ** i for i in range(10)))

    nums_sum = 0
    for num in nums:
        num_str = str(num)
        if all(int(''.join([num_str[i] for i in j])) % rules[j] == 0 for j in rules):
            nums_sum += num
    return nums_sum


if __name__ == '__main__':
    main()
