import re

from utils import sieve


def main():
    primes = sieve(1000000)
    all_primes = set(map(str, primes))
    pattern = re.compile('^[2357][1379]*[37]$')
    candidate_primes = [str(p) for p in primes if re.match(pattern, str(p))]
    sums = 0
    for prime in candidate_primes:
        if all([prime[i:] in all_primes and prime[:i] in all_primes for i in range(1, len(prime))]):
            sums += int(prime)
    print(sums)


if __name__ == '__main__':
    main()
