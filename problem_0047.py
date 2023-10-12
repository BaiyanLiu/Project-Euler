from itertools import count

import utils


def main():
    primes = utils.sieve(5000)
    num_factors = [len(utils.num_factors(i, primes)) for i in range(210, 214)]
    for i in count(214):
        num_factors.append(len(utils.num_factors(i, primes)))
        if all(j == 4 for j in num_factors[-4:]):
            print(i - 3)
            break


if __name__ == '__main__':
    main()
