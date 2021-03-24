from functools import lru_cache
from itertools import count
from math import sqrt
from os import cpu_count
from typing import NamedTuple, Optional


class ContinuedFractionParams(NamedTuple):
    m: int
    d: int
    a: int


def continued_fraction_next_params(i: int, a0: int, prev: ContinuedFractionParams) -> Optional[ContinuedFractionParams]:
    """https://en.wikipedia.org/wiki/Periodic_continued_fraction"""
    m = prev.d * prev.a - prev.m
    if (d := (i - m ** 2) // prev.d) == 0:
        return None
    a = (a0 + m) // d
    return ContinuedFractionParams(m, d, a)


def continued_fraction_num_denom(i: int, n: int, a: list[int]) -> (int, int):
    """https://en.wikipedia.org/wiki/Continued_fraction"""
    if i == n:
        return a[i], 1
    else:
        num, denom = continued_fraction_num_denom(i + 1, n, a)
        return a[i] * num + denom, num


def factorial_series(n: int) -> list[int]:
    nums = [1, 1]
    for i in range(2, n + 1):
        nums.append(nums[i - 1] * i)
    return nums


def hexagonal_nums(start: int, end: int) -> set[int]:
    return {i * (2 * i - 1) for i in range(start, end)}


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def is_permutation(*n: int) -> bool:
    n0 = sorted(str(n[0]))
    return all(sorted(str(i)) == n0 for i in n[1:])


def is_prime(n: int, primes: list[int]) -> bool:
    """https://en.wikipedia.org/wiki/Primality_test"""
    if n < 2:
        return False
    limit = sqrt(n)
    for prime in primes:
        if prime > limit:
            break
        if n % prime == 0:
            return False
    return True


def list_to_chunks(lst: list[int]) -> list[list[int]]:
    chunk_size = len(lst) // (chunks := cpu_count()) + 1
    return [lst[chunk_size * i:chunk_size * (i + 1)] for i in range(chunks)]


def matrix_neighbors(curr: int, matrix: list[int], width: int, has_left: bool = False) -> list[int]:
    neighbors = []
    if (right := curr + 1) % width != 0:
        neighbors.append(right)
    if (down := curr + width) < len(matrix):
        neighbors.append(down)
    if (up := curr - width) > 0:
        neighbors.append(up)
    if (left := curr - 1) % width != width - 1 and has_left and left > 0:
        neighbors.append(left)
    return neighbors


def max_path_triangle(row_start: int, next_row_size: int, nums: list[int], row: list[int]) -> list[int]:
    row = [max(row[i], row[i + 1]) + nums[row_start + i] for i in range(len(row) - 1)]
    if len(row) > 1:
        row = max_path_triangle(row_start - next_row_size, next_row_size - 1, nums, row)
    return row


def num_factors(n: int, primes: list[int]) -> dict[int, int]:
    factors = {}
    # If n = (prime1 ^ a) * (prime2 ^ b), then n has (a + 1) * (b + 1) factors
    for prime in primes:
        if n == 1:
            break
        while n % prime == 0:
            n /= prime
            factors[prime] = factors.get(prime, 1) + 1
    return factors


@lru_cache(maxsize=None)
def num_partitions(n: int) -> int:
    """https://en.wikipedia.org/wiki/Partition_(number_theory)"""
    if n == 0:
        return 1
    partitions = 0
    for i in count(1):
        if (num := pentagonal_num(i)) > n:
            break
        partitions += num_partitions(n - num) * (sign := -1 if i % 2 == 0 else 1)
        if (num := pentagonal_num(-i)) > n:
            break
        partitions += num_partitions(n - num) * sign
    # Small optimization for problem 78
    return partitions % 1000000000


@lru_cache(maxsize=None)
def pentagonal_num(i: int) -> int:
    return i * (3 * i - 1) // 2


def pentagonal_nums(start: int, end: int) -> set[int]:
    return set(map(pentagonal_num, range(start, end)))


def sieve(n: int) -> list[int]:
    """https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
    primes, composites = [2], set()
    for i in range(3, n + 1, 2):
        if i in composites:
            continue
        primes.append(i)
        composites.update({j for j in range(i, n + 1, i)})
    return primes


def square_nums(start: int, end: int) -> set[int]:
    return {i ** 2 for i in range(start, end)}


def sum_divisors(n: int) -> dict[int, int]:
    sums = {}
    for i in range(2, n // 2):
        for j in range(i * 2, n, i):
            sums[j] = sums.get(j, 1) + i
    return sums


def sum_series(n: int) -> int:
    return (n + 1) * n // 2


def totients(n: int) -> dict[int, int]:
    """https://en.wikipedia.org/wiki/Euler's_totient_function"""
    primes_set = set(primes := sieve(n))
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
                for k, v in num_factors(i, primes).items():
                    phi *= values[k] * k ** (v - 2)
                values[i] = phi
            j = 1
            while (k := i ** (j := j + 1)) < n:
                values[k] = values[i] * i ** (j - 1)
    return values


def triangle_nums(start: int, end: int) -> set[int]:
    return {i * (i + 1) // 2 for i in range(start, end)}
