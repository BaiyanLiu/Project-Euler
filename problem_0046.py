import utils


def main():
    primes = utils.sieve(10000)
    squares = {i ** 2 * 2 for i in range(1, 100)}
    divisors = utils.sum_divisors(10000)
    nums = [i for i in range(1, 10000, 2) if i in divisors]
    print(next(i for i in nums if all(i - prime not in squares for prime in primes if prime < i)))


if __name__ == '__main__':
    main()
