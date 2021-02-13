"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?

https://projecteuler.net/problem=42
"""


import argparse


def get_args():
    # noinspection PyTypeChecker
    argparse.ArgumentParser(
        description='Using words.txt, a 16K text file containing nearly two-thousand common English words, how many '
                    'are triangle words?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    get_args()
    words = open('p042_words.txt').read().replace('"', '').split(',')
    triangle_nums = [i * (i + 1) // 2 for i in range(1, 101)]
    offset = ord('A') - 1
    print(len([s for s in words if sum(ord(c) - offset for c in s) in triangle_nums]))


if __name__ == '__main__':
    main()