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
    def count_black_adj(d, i, j):
        return sum((i + di, j + dj) in d
                   for (di, dj) in [
                       (-0.5, +0.5), (0, +1), (+0.5, +0.5),
                       (+0.5, -0.5), (0, -1), (-0.5, -0.5),
                   ])

    today = set(black_tiles(v))
    for _ in range(100):
        min_i, max_i = min(map(lambda t: t[0], today)), max(map(lambda t: t[0], today))
        min_j, max_j = min(map(lambda t: t[1], today)), max(map(lambda t: t[1], today))
        tomorrow = set()
        i = min_i - 0.5
        while i <= max_i + 0.5:
            j = min_j - 1
            while j <= max_j + 0.5:
                is_black = (i, j) in today
                black_adj = count_black_adj(today, i, j)
                if (is_black and 1 <= black_adj <= 2) or (not is_black and black_adj == 2):
                    tomorrow.add((i, j))
                j += 0.5
            i += 0.5
        today = tomorrow
    print(len(today))


with open("input/day24.txt") as f:
    v = [line.replace('\n', '') for line in f]
    part1(v)
    part2(v)
