def black_tiles(v):
    tiles = {}
    for tile in v:
        nes = tile.count('ne')
        ses = tile.count('se')
        nws = tile.count('nw')
        sws = tile.count('sw')
        es = tile.count('e') - nes - ses
        ws = tile.count('w') - nws - sws
        i = 0.5 * (sws + ses - nes - nws)
        j = es - ws + 0.5 * (ses + nes - sws - nws)
        tiles[(i, j)] = not tiles.get((i, j), False)
    return set(t for t, is_black in tiles.items() if is_black)


def part1(v):
    print(len(black_tiles(v)))


def part2(v):
    dirs = [(-0.5, +0.5), (0, +1), (+0.5, +0.5), (+0.5, -0.5), (0, -1), (-0.5, -0.5)]

    def count_black_adj(d, i, j):
        return sum((i + di, j + dj) in d for di, dj in dirs)

    def adjs(i, j):
        return ((i + di, j + dj) for di, dj in dirs)

    today = black_tiles(v)
    for _ in range(100):
        tomorrow = set()
        for black_tile in today:
            if 1 <= count_black_adj(today, *black_tile) <= 2:
                tomorrow.add(black_tile)
            for adj in adjs(*black_tile):
                is_white = adj not in today
                if is_white and count_black_adj(today, *adj) == 2:
                    tomorrow.add(adj)
        today = tomorrow
    print(len(today))


with open("input/day24.txt") as f:
    v = [line.replace('\n', '') for line in f]
    part1(v)
    part2(v)
