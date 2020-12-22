def score(deck):
    return sum((i + 1) * c for i, c in enumerate(deck[::-1]))


def part1(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if card1 >= card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    print(score(deck1 if len(deck1) > 0 else deck2))


def part2(deck1, deck2):
    def play_game(d1, d2):  # returns True if player1 wins the game
        state = set()
        while len(d1) > 0 and len(d2) > 0:

            t = (len(d1), d1[0], d1[-1], len(d2), d2[0], d2[-1])
            if t in state:
                return True
            else:
                state.add(t)

            c1, c2 = d1.pop(0), d2.pop(0)
            if len(d1) >= c1 and len(d2) >= c2:
                p1_wins = play_game(d1[:c1], d2[:c2])
            else:
                p1_wins = c1 >= c2
            if p1_wins:
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)

        return len(d1) > 0

    play_game(deck1, deck2)
    print(score(deck1 if len(deck1) > 0 else deck2))


with open("input/day22.txt") as f:
    d1, d2 = [list(map(int, line.split('\n')[1:])) for line in f.read().split('\n\n')]
    part1(d1[:], d2[:])
    part2(d1, d2)
