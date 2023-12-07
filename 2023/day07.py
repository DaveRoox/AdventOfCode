import functools

HIGH_CARDS = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
FULL_HOUSE = 5
FOUR_OF_A_KIND = 6
FIVE_OF_A_KIND = 7
CARD_VALUE = {c: n for n, c in enumerate(
    ['*', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])}


def hand_type(hand):
    cards, jollies = {}, 0
    for card in hand:
        if card != '*':
            cards[card] = 1 + cards.get(card, 0)
        else:
            jollies += 1

    if jollies == 5 or any(v+jollies == 5 for v in cards.values()):
        return FIVE_OF_A_KIND
    if any(v+jollies == 4 for v in cards.values()):
        return FOUR_OF_A_KIND
    if len(cards.keys()) == 2 and any(v+jollies == 3 for v in cards.values()):
        return FULL_HOUSE
    if len(cards.keys()) == 3 and any(v+jollies == 3 for v in cards.values()):
        return THREE_OF_A_KIND
    if len(cards.keys()) == 3 and any(v == 1 for v in cards.values()):
        return TWO_PAIR
    if len(cards.keys()) == 4:
        return ONE_PAIR
    return HIGH_CARDS


def cmp(hand_bid1, hand_bid2):
    hand1, hand2 = hand_bid1[0], hand_bid2[0]
    t1, t2 = hand_type(hand1), hand_type(hand2)
    if t1 != t2:
        return t1 - t2
    for card1, card2 in zip(hand1, hand2):
        if card1 != card2:
            return CARD_VALUE[card1] - CARD_VALUE[card2]
    return 0


def part1(hand_bid_pairs):
    print(sum((i+1) * hb[1]
          for i, hb in enumerate(sorted(hand_bid_pairs, key=functools.cmp_to_key(cmp)))))


def part2(hand_bid_pairs):
    hand_bid_pairs = list(
        map(lambda hb: (hb[0].replace('J', '*'), hb[1]), hand_bid_pairs))
    print(sum((i+1) * hb[1]
          for i, hb in enumerate(sorted(hand_bid_pairs, key=functools.cmp_to_key(cmp)))))


with open("input/day07.txt") as f:
    hand_bid_pairs = list(map(lambda t: (t[0], int(t[1])), map(
        lambda l: tuple(l.replace('\n', '').split()), f.readlines())))
    part1(hand_bid_pairs)
    part2(hand_bid_pairs)
