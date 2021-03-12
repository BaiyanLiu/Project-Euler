"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))

By expanding this for the first four iterations, we get:

1 + 1 / 2 = 3 / 2 = 1.5
1 + 1 / (2 + 1 / 2) = 7 / 5 = 1.4
1 + 1 / (2 + 1 / (2 + 1 / 2)) = 17 / 12 = 1.41666...
1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / 2))) = 41 / 29 = 1.41379...

The next three expansions are 90 / 70, 230 / 169, and 577 / 408, but the eighth expansion, 1303 / 985, is the first
example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

https://projecteuler.net/problem=57
"""


def main():
    numerator, denominator = [1, 3], [1, 2]
    for i in range(1, 1000):
        numerator.append(numerator[i] * 2 + numerator[i - 1])
        denominator.append(denominator[i] * 2 + denominator[i - 1])
    print(sum(1 for i in range(1000) if len(str(numerator[i])) > len(str(denominator[i]))))


if __name__ == '__main__':
    main()
