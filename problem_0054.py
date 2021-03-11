"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example,
a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a
pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the
next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand    Player 1            Player 2	    Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD  Player 2
        Pair of Fives       Pair of Eights
2       5D 8C 9S JS AC      2C 5C 7D 8S QH  Player 1
        Highest card Ace    Highest card Queen
3       2D 9C AS AH AC      3D 6D 7D TD QD  Player 2
        Three Aces          Flush with Diamonds
4       4D 6S 9H QH QC      3D 6D 7H QD QS  Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven
5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D  Player 1
        Full House          Full House
        With Three Fours    With Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten
cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific
order, and in each hand there is a clear winner.

How many hands does Player 1 win?

https://projecteuler.net/problem=54
"""


class Card:
    def __init__(self, card):
        self.value = card[:2]
        self.suit = card[2]

    def __lt__(self, other):
        return self.value < other.value


def main():
    card_trans = str.maketrans({'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'})
    hands = open('p054_poker.txt').read().translate(card_trans).rstrip().split('\n')
    count = 0
    for hand in hands:
        hand = [Card(c.zfill(3)) for c in hand.split(' ')]
        if hand_value(hand[:5]) > hand_value(hand[5:]):
            count += 1
    print(count)


def hand_value(hand: list[Card]) -> str:
    hand = list(reversed(sorted(hand)))

    is_straight = all([int(hand[0].value) - int(hand[i].value) == i for i in range(1, 5)])
    if is_flush := all(card.suit == hand[0].suit for card in hand):
        if hand[0].value == '14':
            return '9-RoyalFlush-'
        elif is_straight:
            return '8-StraightFlush-' + hand[0].value

    counts = {}
    for card in hand:
        counts[card.value] = counts.get(card.value, 0) + 1
    num_counts = len(counts)

    if 4 in counts.values():
        return '7-4oak-' + card_for_count(counts, 4) + list(counts.keys())[0]
    elif num_counts == 2:
        return '6-FullHouse-' + card_for_count(counts, 3) + list(counts.keys())[0]
    elif is_flush:
        return '5-Flush-' + all_values(hand)
    elif is_straight:
        return '4-Straight-' + hand[0].value
    elif 3 in counts.values():
        return '3-3oak-' + card_for_count(counts, 3) + all_values_str(list(counts.keys()))
    elif num_counts == 3:
        pair_1, pair_2 = card_for_count(counts, 2), card_for_count(counts, 2)
        return '2-TwoPairs-' + all_values_str([pair_1, pair_2]) + list(counts.keys())[0]
    elif num_counts == 4:
        return '1-OnePair-' + card_for_count(counts, 2) + all_values_str(list(counts.keys()))
    else:
        return '0-HighCard-' + all_values(hand)


def card_for_count(counts: dict[str, int], value: int) -> str:
    counts.pop(key := next(k for k in counts.keys() if counts[k] == value))
    return key


def all_values(cards: list[Card]) -> str:
    return ''.join([c.value for c in cards])


def all_values_str(values: list[str]) -> str:
    return ''.join(list(reversed(sorted(values))))


if __name__ == '__main__':
    main()
