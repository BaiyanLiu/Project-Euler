"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

https://projecteuler.net/problem=60
"""


import argparse
from sys import maxsize

import utils


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Find the lowest sum for a set of n primes for which any two primes concatenate to produce '
                    'another prime.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of primes')
    return parser.parse_args()


def main():
    args = get_args()
    primes = utils.sieve(10000)
    candidates = {}
    for i in primes:
        for j_str in [str(p) for p in primes if p > i]:
            if utils.is_prime(int((i_str := str(i)) + j_str), primes) and utils.is_prime(int(j_str + i_str), primes):
                candidates[i_str] = candidates.get(i_str, set()) | {j_str}
                candidates[j_str] = candidates.get(j_str, set()) | {i_str}
    candidates = {k: v for k, v in candidates.items() if len(v) >= args.n - 1}
    print(min(min_sum_primes({k}, v, candidates, args.n) for k, v, in candidates.items()))


def min_sum_primes(keys: set[str], values: set[str], candidates: dict[str, set[str]], n: int) -> int:
    if len(keys) == n:
        return sum(map(int, keys))
    else:
        min_sum = maxsize
        for v in [v for v in values if v not in keys and v in candidates]:
            min_sum = min(min_sum, min_sum_primes(keys | {v}, values & candidates[v], candidates, n))
        return min_sum


if __name__ == '__main__':
    main()
