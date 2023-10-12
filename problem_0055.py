from utils import is_palindrome


def main():
    nums = []
    for i in range(1, 10000):
        n = i
        for j in range(50):
            if is_palindrome(str(n := reverse_and_add(n))):
                nums.append(i)
                break
    print(9999 - len(nums))


def reverse_and_add(n: int) -> int:
    return n + int(str(n)[::-1])


if __name__ == '__main__':
    main()
