"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for
example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

https://projecteuler.net/problem=32
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='Find the sum of all products whose multiplicand/multiplier/product identity can be written as a '
                    '1 through 9 pandigital.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    nums = set()
    for i in range(1, 9876):
        if i % 10 <= 1:
            continue
        if len(i_str := str(i)) != len(''.join(set(i_str))) or '0' in i_str:
            continue
        for j in range(i, 9876):
            if (prod := i * j) > 9876 or j % 10 <= 1:
                continue
            if len(num_str := str(i) + str(j) + str(prod)) == len(''.join(set(num_str))) == 9 and '0' not in num_str:
                nums.add(prod)
    print(sum(nums))


if __name__ == '__main__':
    main()
