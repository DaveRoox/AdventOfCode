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


def chain(tile_id, tiles_by_id, grid, taken, i=0, j=0):
    taken.add(tile_id)
    tile = tiles_by_id[tile_id]
    if i not in grid:
        grid[i] = {}
    grid[i][j] = tile

    def matches(tile, other_tile_id, s):
        for other_tile in transform(tiles_by_id[other_tile_id]):
            if s == 0:
                check = tile[0] == other_tile[-1]
            elif s == 1:
                check = ''.join(t[-1] for t in tile) == ''.join(t[0] for t in other_tile)
            elif s == 2:
                check = tile[-1] == other_tile[0]
            else:  # s == 3
                check = ''.join(t[0] for t in tile) == ''.join(t[-1] for t in other_tile)
            if check:
                tiles_by_id[other_tile_id] = other_tile
                return True
        return False

    for side, (di, dj) in enumerate(((-1, 0), (0, +1), (+1, 0), (0, -1))):  # top, right, bottom and left
        for other_tile_id in tiles_by_id.keys():
            if other_tile_id not in taken:
                if matches(tile, other_tile_id, side):
                    chain(other_tile_id, tiles_by_id, grid, taken, i + di, j + dj)
                    break  # side matched


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

    grid = {}
    chain(list(tiles_by_id.keys())[0], tiles_by_id, grid, set())  # filling the grid
    g = fold_tiles_and_remove_borders(grid)
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
