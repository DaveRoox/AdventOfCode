def part1(cards):
    print(sum(map(lambda card: int(2 ** (len(set.intersection(*card)) - 1)), cards)))

def part2(cards):
    cards_m = { i: 1 for i in range(len(cards))}
    for i, card in enumerate(cards):
        s1, s2 = card
        n = len(set(s1).intersection(s2))
        for j in range(i+1, min(i+n+1, len(cards_m))):
            cards_m[j] = cards_m[j]+cards_m[i]
    print(sum(cards_m.values()))

with open("input/day04.txt") as f:
    # (Final) Transform input from:
    # 'Card   A: n1 n2 ... nN | m1 m2 ... mM'
    # to:
    # [[ { n1 n2 ... nN }, { m1 m2 ... mM } ]]
    cards = list(
        # (3) Transform input from:
        # [ 'n1 n2 ... nN', 'm1 m2 ... mM' ]
        # to:
        # [ { n1 n2 ... nN }, { m1 m2 ... mM } ]
        map(
            lambda v: list(
                # (2) Transform input from:
                # 'n1 n2 ... nN'
                # to:
                # { n1 n2 ... nN }
                map(
                    lambda nums: set(map(int, nums.split())),
                    v
                )
            ),
            # (1) Transform input from:
            # 'Card   A: n1 n2 ... nN | m1 m2 ... mM'
            # to:
            # [ 'n1 n2 ... nN', 'm1 m2 ... mM' ]
            map(
                lambda l: l.replace('\n', '').split(': ')[1].split(' | '),
                f.readlines()
            )
        )
    )
    part1(cards)
    part2(cards)
