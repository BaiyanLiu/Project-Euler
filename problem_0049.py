import utils


def main():
    primes = set([p for p in utils.sieve(10000) if p >= 1000 and p not in {1487, 4817, 8147}])
    for i in primes:
        for j in [p for p in primes if p > i]:
            if (k := j + j - i) in primes and utils.is_permutation(i, j, k):
                print(f'{i}{j}{k}')
                break


if __name__ == '__main__':
    main()
