def main():
    num, denom = [1, 3], [1, 2]
    for i in range(1, 1000):
        num.append(num[i] * 2 + num[i - 1])
        denom.append(denom[i] * 2 + denom[i - 1])
    print(sum(1 for i in range(1000) if len(str(num[i])) > len(str(denom[i]))))


if __name__ == '__main__':
    main()
