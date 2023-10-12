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
