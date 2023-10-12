import argparse
from math import isqrt

from utils import sieve


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='How many numbers below n can be expressed as the sum of a prime square, prime cube, and prime '
                    'fourth power?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Upper limit (exclusive)')
    return parser.parse_args()


def main():
    args = get_args()
    primes = sieve(isqrt(args.n))
    max_3, max_4 = args.n ** (1 / 3), args.n ** (1 / 4)
    primes_3 = [i ** 3 for i in primes if i < max_3]
    primes_4 = [i ** 4 for i in primes if i < max_4]
    nums = set()
    for i in [i ** 2 for i in primes]:
        for j in primes_3:
            if i + j >= args.n:
                break
            for k in primes_4:
                if (num := i + j + k) >= args.n:
                    break
                nums.add(num)
    print(len(nums))


if __name__ == '__main__':
    main()
