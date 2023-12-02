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
    print(sum(map(lambda e: reduce(lambda v, acc: v * acc, e.values(), 1), games.values())))


with open("input/day02.txt") as f:
    games = dict(
        map(
            lambda kv: (
                int(kv[0].split()[1]),
                (lambda v: dict(sorted(map(lambda e: (e[0], int(e[1])), v), key=lambda e: e[1])))(
                    map(
                        lambda e: e.split()[::-1],
                        kv[1].split(', ')
                    )
                )
            ),
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
