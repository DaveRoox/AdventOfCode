def find_offsets(grid, offset):
    rows, cols = [0], [0]
    for i in range(len(grid)):
        rows.append(rows[-1])
        if all(cell == '.' for cell in grid[i]):
            rows[-1] += offset
    for j in range(len(grid[0])):
        cols.append(cols[-1])
        if all(grid[i][j] == '.' for i in range(len(grid))):
            cols[-1] += offset
    return rows[1:], cols[1:]


def shifted_galaxy(galaxy, rows_offsets, cols_offsets):
    return (galaxy[0] + rows_offsets[galaxy[0]], galaxy[1] + cols_offsets[galaxy[1]])


def sum_distances(grid, offset):
    galaxies = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == '#']
    rows_offsets, cols_offsets = find_offsets(grid, offset)
    res = 0
    for g1 in range(len(galaxies)):
        galaxy1 = shifted_galaxy(galaxies[g1], rows_offsets, cols_offsets)
        for g2 in range(g1+1, len(galaxies)):
            galaxy2 = shifted_galaxy(galaxies[g2], rows_offsets, cols_offsets)
            res += abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])
    return res


def part1(grid):
    print(sum_distances(grid, offset=1))


def part2(grid):
    print(sum_distances(grid, offset=1000000-1))


with open("input/day11.txt") as f:
    grid = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    part1(grid)
    part2(grid)
