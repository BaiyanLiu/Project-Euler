"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
with (1,2, ... , n) where n > 1?

https://projecteuler.net/problem=38
"""


def main():
    max_num = 0
    for i in range(1, 9876):
        num = ''
        for j in range(1, 10):
            num += str(i * j)
            if not(len(num) == len(set(num)) <= 9) or '0' in num:
                break
            elif len(num) == 9:
                max_num = max(max_num, int(num))
                break
    print(max_num)


if __name__ == '__main__':
    main()
