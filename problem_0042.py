from utils import triangle_nums


def main():
    words = open('input/p042_words.txt').read().replace('"', '').split(',')
    offset = ord('A') - 1
    print(len([s for s in words if sum(ord(c) - offset for c in s) in triangle_nums(1, 101)]))


if __name__ == '__main__':
    main()
