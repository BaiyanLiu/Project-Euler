def main():
    names = sorted(open('input/p022_names.txt').read().replace('"', '').split(','))
    sums = 0
    offset = ord('A') - 1
    for i in range(len(names)):
        sums += sum([ord(c) - offset for c in names[i]]) * (i + 1)
    print(sums)


if __name__ == '__main__':
    main()
