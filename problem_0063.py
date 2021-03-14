"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

https://projecteuler.net/problem=63
"""


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
