from utils import factorial_series


def main():
    nums = factorial_series(100)
    print(sum(1 for i in range(23, 101) for j in range(i + 1) if nums[i] // (nums[j] * nums[i - j]) > 1000000))


if __name__ == '__main__':
    main()
