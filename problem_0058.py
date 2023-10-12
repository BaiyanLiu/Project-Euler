from itertools import count

import utils


def main():
    primes = utils.sieve(100000)
    num_primes = 0
    for i in count(3, 2):
        i2 = i ** 2
        num_primes += sum(1 for k in (i2 - (i - 1) * j for j in range(1, 4)) if utils.is_prime(k, primes))
        if num_primes / (i * 2 - 1) < 0.1:
            print(i)
            break


if __name__ == '__main__':
    main()
