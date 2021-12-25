def can_move_east(g, i, j):
    return g[i][j] == '>' and g[i][(j + 1) % len(g[0])] == '.'


def can_move_south(g, i, j):
    return g[i][j] == 'v' and (
            g[(i + 1) % len(g)][j] == '.' or
            g[(i + 1) % len(g)][j] == '>' and can_move_east(g, (i + 1) % len(g), j)
    ) and not can_move_east(g, (i + 1) % len(g), (j - 1 + len(g[0])) % len(g[0]))


def step(g):
    to_move_east = set()
    to_move_south = set()
    for i in range(0, len(g)):
        for j in range(0, len(g[0])):
            if can_move_east(g, i, j):
                to_move_east.add((i, j))
            if can_move_south(g, i, j):
                to_move_south.add((i, j))
    for (i, j) in to_move_east:
        g[i][j], g[i][(j + 1) % len(g[0])] = '.', '>'
    for (i, j) in to_move_south:
        g[i][j], g[(i + 1) % len(g)][j] = '.', 'v'
    return len(to_move_south) + len(to_move_east)


def part1(g):
    c = 1
    while step(g) > 0:
        c += 1
    print(c)


def part2(_):
    print('Merry Christmas!')


with open("input/day25.txt") as f:
    v = list(map(lambda l: list(l.replace('\n', '')), f.readlines()))
    part1(v)
    part2(v)
