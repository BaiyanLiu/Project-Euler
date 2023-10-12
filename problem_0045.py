import utils


def main():
    tri_nums = utils.triangle_nums(286, 100000)
    pen_nums = utils.pentagonal_nums(166, 100000)
    hex_nums = utils.hexagonal_nums(144, 100000)
    print(min(tri_nums & pen_nums & hex_nums))


if __name__ == '__main__':
    main()
