import argparse
import concurrent.futures
from os import cpu_count
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
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = [executor.submit(generate_candidates, chunk, primes) for chunk in utils.list_to_chunks(primes)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            for k, v in result.items():
                if k not in candidates:
                    candidates[k] = set()
                candidates[k].update(v)
    candidates = {k: v for k, v in candidates.items() if len(v) >= args.n - 1}
    print(min(min_sum_primes({k}, v, candidates, args.n) for k, v, in candidates.items()))


def generate_candidates(primes_chunk: list[int], primes: list[int]) -> dict[str, set[str]]:
    candidates = {}
    for i in primes_chunk:
        i_str = str(i)
        for j_str in [str(p) for p in primes if p > i]:
            if utils.is_prime(int(i_str + j_str), primes) and utils.is_prime(int(j_str + i_str), primes):
                add_candidate(i_str, j_str, candidates)
                add_candidate(j_str, i_str, candidates)
    return candidates


def add_candidate(k: str, v: str, candidates: dict[str, set[str]]) -> None:
    if k not in candidates:
        candidates[k] = set()
    candidates[k].add(v)


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
