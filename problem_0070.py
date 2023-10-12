from sys import maxsize

import utils


def main():
    limit = 10000000
    primes = utils.sieve(limit // 2)
    min_n, min_v = 0, maxsize
    for i in primes:
        for j in primes:
            if (n := i * j) > limit:
                break
            phi = (i - 1) * (j - 1)
            if (v := n / phi) < min_v and utils.is_permutation(n, phi):
                min_n, min_v = n, v
    print(min_n)


if __name__ == '__main__':
    main()
