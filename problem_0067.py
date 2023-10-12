from utils import max_path_triangle


def main():
    nums = list(map(int, open('input/p067_triangle.txt').read().split()))
    print(max_path_triangle(-100 - 99, 98, nums, nums[-100:])[0])


if __name__ == '__main__':
    main()
