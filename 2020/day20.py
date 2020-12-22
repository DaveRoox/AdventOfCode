import operator
from functools import reduce


def transform(tile):
    def flip():
        return [line[::-1] for line in tile]

    def rotate():
        return [''.join([tile[i][j] for i in range(len(tile))][::-1]) for j in range(len(tile[0]))]

    yield tile
    yield flip()
    tile = rotate()
    yield tile
    yield flip()
    tile = rotate()
    yield tile
    yield flip()
    tile = rotate()
    yield tile
    yield flip()


def chain(tiles_by_id):
    visited, grid, q = set(), dict(), [(list(tiles_by_id.keys())[0], 0, 0)]
    while q:
        tile_id, i, j = q.pop()
        visited.add(tile_id)
        tile = tiles_by_id[tile_id]
        if i not in grid:
            grid[i] = {}
        grid[i][j] = tile
        sides_matched = 0
        for other_tile_id in tiles_by_id:
            if other_tile_id not in visited:
                for other_tile in transform(tiles_by_id[other_tile_id]):
                    for di, dj, check in [
                        (-1, 0, tile[0] == other_tile[-1]),
                        (0, +1, ''.join(t[-1] for t in tile) == ''.join(t[0] for t in other_tile)),
                        (+1, 0, tile[-1] == other_tile[0]),
                        (0, -1, ''.join(t[0] for t in tile) == ''.join(t[-1] for t in other_tile)),
                    ]:
                        if check:
                            tiles_by_id[other_tile_id] = other_tile
                            sides_matched += 1
                            q.append((other_tile_id, i + di, j + dj))
                if sides_matched == 4:
                    break
    return grid


def part1(tiles_by_id):
    def has_pluggable_tile(tiles, curr_tile_id, value):
        inv_value = value[::-1]
        for tile_id, tile in tiles.items():
            if tile_id != curr_tile_id:
                if value in tile or inv_value in tile:
                    return True
        return False

    def count_pluggable(tiles, curr_tile_id):
        return sum(has_pluggable_tile(tiles, curr_tile_id, tile_value) for tile_value in tiles[curr_tile_id])

    tile_sides_by_id = {
        tile_id: [tile[0], ''.join(t[-1] for t in tile), tile[-1], ''.join(t[0] for t in tile)]
        for tile_id, tile in tiles_by_id.items()
    }
    print(reduce(operator.mul, (id for id in tile_sides_by_id if count_pluggable(tile_sides_by_id, id) == 2), 1))


def part2(tiles_by_id):
    def fold_tiles_and_remove_borders(grid):
        final_grid = []
        for r in sorted(grid.keys()):
            tiles = [grid[r][c] for c in sorted(grid[r].keys())]
            for i in range(1, len(tiles[0]) - 1):
                final_grid.append(''.join(tile[i][1:-1] for tile in tiles))
        return final_grid

    def matches_pattern(g, i, j):
        for prow in range(len(pattern)):
            for pcol in range(len(pattern[0])):
                if pattern[prow][pcol] == '#':
                    if g[i + prow][j + pcol] != '#':
                        return False
        return True

    g = fold_tiles_and_remove_borders(chain(tiles_by_id))
    pattern = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    for g in transform(g):
        monsters = 0
        for i in range(len(g) - len(pattern)):
            for j in range(len(g[0]) - len(pattern[0])):
                if matches_pattern(g, i, j):
                    monsters += 1
        if monsters > 0:
            print(sum(line.count('#') for line in g) - monsters * sum(line.count('#') for line in pattern))


with open("input/day20.txt") as f:
    t = {int(tile[0].split()[1][:-1]): tile[1:] for tile in (l.split('\n') for l in f.read().strip().split('\n\n'))}
    part1(t)
    part2(t)
