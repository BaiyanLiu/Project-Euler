"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

https://projecteuler.net/problem=36
"""


from utils import is_palindrome


def main():
    print(sum([i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(bin(i)[2:])]))


if __name__ == '__main__':
    main()
