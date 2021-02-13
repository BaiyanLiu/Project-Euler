"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

https://projecteuler.net/problem=22
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='What is the total of all the name scores in the file?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    names = sorted(open('p022_names.txt').read().replace('"', '').split(','))
    sums = 0
    offset = ord('A') - 1
    for i in range(len(names)):
        sums += sum([ord(c) - offset for c in names[i]]) * (i + 1)
    print(sums)


if __name__ == '__main__':
    main()