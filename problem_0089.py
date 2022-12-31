"""
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even
though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in
valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this
problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

https://projecteuler.net/problem=89
"""


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
