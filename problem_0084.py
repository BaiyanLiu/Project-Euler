import argparse
from itertools import product


CC = {2, 17, 33}
CH = {7, 22, 36}
GO, G2J, JAIL = 0, 30, 10
C1, E3, H2 = 11, 24, 39
R = [5, 15, 25, 35]
U = [12, 28]


def get_args():
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='If two n-sided dice are used, find the six-digit modal string.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Number of sides on the dice')
    return parser.parse_args()


def main():
    args = get_args()
    dice_chance = dict.fromkeys(range(2, args.n * 2 + 1), 0)
    roll_chance = 1 / args.n ** 2
    three_doubles = roll_chance ** 2
    for d1, d2 in product(range(1, args.n + 1), range(1, args.n + 1)):
        dice_chance[(value := d1 + d2)] += roll_chance
        if d1 == d2:
            dice_chance[value] -= three_doubles

    board = (old_board := dict.fromkeys(range(40), 0)).copy()
    board[GO] = 100
    while any(abs(old - new) > 0.000001 for old, new in zip(old_board.values(), board.values())):
        old_board.update(board)
        roll_dice(dice_chance, board)
    print(''.join(reversed([str(i).zfill(2) for i in sorted(board, key=board.get)[-3:]])))


def roll_dice(dice_chance: dict[int, float], board: dict[int, float]) -> None:
    delta = dict.fromkeys(range(40), 0)
    for square in board:
        jail_chance = board[square]
        for k, v in dice_chance.items():
            delta[(square + k) % 40] += (chance := board[square] * v)
            jail_chance -= chance
        delta[JAIL] += jail_chance
        delta[square] -= board[square]
    for square in board:
        board[square] += delta[square]
    update_board(board)


def update_board(board: dict[int, float]) -> None:
    for square in board:
        dest_chance = board[square] * 1 / 16
        if square in CC:
            update_for_cc(square, board, dest_chance)
        elif square in CH:
            for dest in [GO, JAIL, C1, E3, H2, R[0], square - 3]:
                board[dest] += dest_chance
            if square - 3 in CC:
                update_for_cc(square - 3, board, dest_chance * 1 / 16)
            board[next(iter(r for r in R if r > square), R[0])] += dest_chance * 2
            board[next(iter(u for u in U if u > square), U[0])] += dest_chance
            board[square] -= dest_chance * 10
        elif square == G2J:
            board[JAIL] += board[G2J]
            board[G2J] = 0


def update_for_cc(square: int, board: dict[int, float], dest_chance: float) -> None:
    board[GO] += dest_chance
    board[JAIL] += dest_chance
    board[square] -= dest_chance * 2


if __name__ == '__main__':
    main()
