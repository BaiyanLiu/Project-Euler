"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

https://projecteuler.net/problem=77
"""


from functools import lru_cache
from itertools import count

from utils import sieve


def main():
    primes = tuple(reversed(sieve(100)))
    print(next(i for i in count(2) if num_partitions(i, 2, primes) > 5000))


@lru_cache(maxsize=None)
def num_partitions(n: int, curr_p: int, primes: tuple) -> int:
    if n == 0:
        return 1
    elif n < 2:
        return 0
    partitions = 0
    for p in primes:
        if p > n:
            continue
        if p < curr_p:
            break
        partitions += num_partitions(n - p, p, primes)
    return partitions


if __name__ == '__main__':
    main()
