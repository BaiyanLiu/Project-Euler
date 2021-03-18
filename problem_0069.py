"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less
than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.
n 	Relatively Prime 	φ(n) 	n/φ(n)
2 	1 	1 	2
3 	1,2 	2 	1.5
4 	1,3 	2 	2
5 	1,2,3,4 	4 	1.25
6 	1,5 	2 	3
7 	1,2,3,4,5,6 	6 	1.1666...
8 	1,3,5,7 	4 	2
9 	1,2,4,5,7,8 	6 	1.5
10 	1,3,7,9 	4 	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

https://projecteuler.net/problem=69
"""


import argparse

import utils


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the value of n ≤ a for which n/φ(n) is a maximum.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('a', type=int, help='Upper limit (inclusive')
    return parser.parse_args()


def main():
    args = get_args()
    print(max(values := {n: n / phi for n, phi in totients(args.a).items()}, key=values.get))


def totients(n: int) -> dict[int, int]:
    """https://en.wikipedia.org/wiki/Euler's_totient_function"""
    primes = utils.sieve(n)
    primes_set = set(primes)
    values = {}
    for i in range(2, n + 1):
        if i not in values:
            if i in primes_set:
                values[i] = i - 1
                for j in range(2, i):
                    if (k := i * j) >= n:
                        break
                    values[k] = values[i] * values[j]
            else:
                phi = 1
                for k, v in utils.num_factors(i, primes).items():
                    phi *= values[k] * k ** (v - 2)
                values[i] = phi
            j = 1
            while (k := i ** (j := j + 1)) < n:
                values[k] = values[i] * i ** (j - 1)
    return values


if __name__ == '__main__':
    main()
