class Card:
    def __init__(self, card: str):
        self.value = card[:2]
        self.suit = card[2]

    def __lt__(self, other):
        return self.value < other.value


def main():
    card_trans = str.maketrans({'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'})
    hands = open('input/p054_poker.txt').read().translate(card_trans).rstrip().split('\n')
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
