import re
from itertools import count


def main():
    file = open('input/p079_keylog.txt').read()
    keys = {tuple(k) for k in file.split()}
    chars = {c for c in file if c.isdigit()}
    chars_str = ''.join(sorted(chars))
    patterns = [re.compile(f'[{chars_str}]*'.join(k)) for k in keys]
    first = next(c for c in chars if all(c not in k[1:] for k in keys))
    second = next(c for c in chars if c != first and all(c not in k[2:] for k in keys))
    last = next(c for c in chars if all(c not in k[:2] for k in keys))
    second_last = next(c for c in chars if c != last and all(c not in k[:1] for k in keys))
    for i in count(int(first + second + '0' * (len(chars) - 4) + second_last + last), 100):
        i_str = str(i)
        if all(p.search(i_str) for p in patterns):
            print(i)
            break


if __name__ == '__main__':
    main()
