from math import sqrt
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
    chunk_size = len(lst) // 6 + 1
    return [lst[chunk_size * i:chunk_size * (i + 1)] for i in range(6)]


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


def pentagonal_nums(start: int, end: int) -> set[int]:
    return {i * (3 * i - 1) // 2 for i in range(start, end)}


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


def triangle_nums(start: int, end: int) -> set[int]:
    return {i * (i + 1) // 2 for i in range(start, end)}
