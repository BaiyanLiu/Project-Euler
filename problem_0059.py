from itertools import product


def main():
    encrypted = list(map(int, open('input/p059_cipher.txt').read().split(',')))
    invalid_chars = {ord('`'), ord('~')}
    key_range = range(ord('a'), ord('z') + 1)
    for key in product(key_range, key_range, key_range):
        decrypted = [encrypted[i] ^ key[i % 3] for i in range(len(encrypted))]
        if all(chr(d).isprintable() and d not in invalid_chars for d in decrypted):
            print(sum(decrypted))
            break


if __name__ == '__main__':
    main()
