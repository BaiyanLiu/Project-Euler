from utils import sieve


def main():
    primes = reversed(sieve(7654321))
    print(next(p for p in primes if is_pandigital(p)))


def is_pandigital(n: int) -> bool:
    n_len = len(n_str := str(n))
    return '0' not in n_str and n_len == len(set(n_str)) and max(n_str) == str(n_len)


if __name__ == '__main__':
    main()
