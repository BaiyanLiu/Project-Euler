def main():
    nums = set()
    for i in range(1, 9876):
        if i % 10 <= 1:
            continue
        if '0' in (i_str := str(i)) or len(i_str) != len(''.join(set(i_str))):
            continue
        for j in range(i, 9876):
            if j % 10 <= 1:
                continue
            if (prod := i * j) > 9876:
                break
            num_str = str(i) + str(j) + str(prod)
            if '0' not in num_str and len(num_str) == len(''.join(set(num_str))) == 9:
                nums.add(prod)
    print(sum(nums))


if __name__ == '__main__':
    main()
