from math import sqrt


def factorial_series(n: int) -> list[int]:
    nums = [1, 1]
    for i in range(2, n + 1):
        nums.append(nums[i - 1] * i)
    return nums


def hexagonal_nums(start: int, end: int) -> set[int]:
    return {i * (2 * i - 1) for i in range(start, end)}


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


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


def num_factors(n: int, primes: list[int]) -> dict[int, int]:
    factors = {}
    # If n = (prime1 ^ a) * (prime2 ^ b), then n has (a + 1) * (b + 1) factors
    for prime in primes:
        while n % prime == 0:
            n /= prime
            factors[prime] = factors.get(prime, 1) + 1
    return factors


def pentagonal_nums(start: int, end: int) -> set[int]:
    return {i * (3 * i - 1) // 2 for i in range(start, end)}


def sieve(n: int) -> list[int]:
    """https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
    nums = [2]
    nums.extend(range(3, n + 1, 2))
    i, limit = 2, sqrt(n)
    while (i := next(x for x in nums if x > i)) <= limit:
        i2 = i ** 2
        nums = [x for x in nums if x < i2 or x % i != 0]
    return nums


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
