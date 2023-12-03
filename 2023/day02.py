from functools import reduce


def part1(games):
    constraints = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    print(sum(map(
        lambda game: game[0],
        filter(
            lambda game: all(map(
                lambda kv: kv[1] >= game[1].get(kv[0], 0),
                constraints.items())),
            games.items()))))


def part2(games):
    print(sum(map(lambda e: reduce(int.__mul__, e.values()), games.values())))


with open("input/day02.txt") as f:
    # (Final) Transform input from:
    # 'Game A: X1a color1, ..., XNa colorN; ... ; X1k color1, ..., XNk colorN'
    # to:
    # { A: { 'color1': max(X1a, ..., X1k), ..., 'colorN': max(XNa, ..., XNk) } }
    games = dict(
        # (4) Transform input from:
        # { 'Game A': '%d color1, ..., %d colorN, ... , %d color1, ..., %d colorN' }
        # to:
        # { A: { 'color1': max(X1a, ..., X1k), ..., 'colorN': max(XNa, ..., XNk) } }
        map(
            lambda kv: (
                int(kv[0].split()[1]),
                # (3) Transform input from:
                # [['color1', X1a'], ..., ['colorN', 'XNa'], ..., ['color1', 'X1k'], ..., ['colorN', 'XNk']]
                # to:
                # { 'color1': max(X1a, ..., X1k), ..., 'colorN': max(XNa, ..., XNk) }
                (lambda v: dict(sorted(map(lambda e: (e[0], int(e[1])), v), key=lambda e: e[1])))(
                    # (2) Transform input from:
                    # 'X1a color1, ..., XNa colorN, ... , X1k color1, ..., XNk colorN'
                    # to:
                    # [['color1', X1a'], ..., ['colorN', 'XNa'], ..., ['color1', 'X1k'], ..., ['colorN', 'XNk']]
                    map(
                        lambda e: e.split()[::-1],
                        kv[1].split(', ')
                    )
                )
            ),
            # (1) Transform input from:
            # 'Game A: X1a color1, ..., XNa colorN; ... ; X1k color1, ..., XNk colorN'
            # to:
            # { 'Game A': 'X1a color1, ..., XNa colorN, ... , X1k color1, ..., XNk colorN' }
            dict(
                map(
                    lambda l: l.replace('\n', '').replace(';', ',').split(': '),
                    f.readlines()
                )
            ).items()
        )
    )
    part1(games)
    part2(games)
