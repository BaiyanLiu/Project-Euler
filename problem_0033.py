"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

https://projecteuler.net/problem=33
"""


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
