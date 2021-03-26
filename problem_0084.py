"""
In the game, Monopoly, the standard board is set up in the following way:
p084_monopoly_board.png

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they
advance in a clockwise direction. Without any further rules we would expect to visit each square with equal
probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this
distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player
rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to
jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from
the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There
are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a
movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL
    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of
finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which
the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a
movement to another square, and it is the final square that the player finishes at on each roll that we are
interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore
the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to
produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = square 10,
E3 (3.18%) = square 24, and GO (3.09%) = square 00. So these three most popular squares can be listed with the
six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

https://projecteuler.net/problem=84
"""


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
