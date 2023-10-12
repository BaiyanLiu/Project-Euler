from itertools import count


def main():
    nums = 0
    for i in count(1):
        if num := sum(1 for j in range(1, 10) if len(str(j ** i)) == i):
            nums += num
        else:
            break
    print(nums)


if __name__ == '__main__':
    main()
