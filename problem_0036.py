from utils import is_palindrome


def main():
    print(sum([i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(bin(i)[2:])]))


if __name__ == '__main__':
    main()
