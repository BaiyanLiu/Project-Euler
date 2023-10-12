import argparse
import re

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many circular primes are there below n?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    primes = sieve(args.n)
    pattern = re.compile('^[1379]+$')
    primes = [str(p) for p in primes if re.match(pattern, str(p))]
    circular_primes = ['2', '3', '5']
    for prime in primes:
        if prime in circular_primes:
            continue
        perms = {prime[i:] + prime[:i] for i in range(len(prime))}
        if all([i in primes for i in perms]):
            circular_primes.extend([i for i in perms if i in primes])
    print(len(circular_primes))


if __name__ == '__main__':
    main()
