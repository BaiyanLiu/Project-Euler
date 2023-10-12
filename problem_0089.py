def main():
    char_saved = 0
    for numeral in open('input/p089_roman.txt').read().split():
        new_numeral = numeral.replace('DCCCC', 'CM').replace('LXXXX', 'XC').replace('VIIII', 'IX')
        if 'CCCC' in new_numeral and 'D' not in new_numeral:
            char_saved += 2
        if 'XXXX' in new_numeral and 'L' not in new_numeral:
            char_saved += 2
        if 'IIII' in new_numeral and 'V' not in new_numeral:
            char_saved += 2
        char_saved += len(numeral) - len(new_numeral)
    print(char_saved)


if __name__ == '__main__':
    main()
