from functools import reduce


def find_adj_nums(grid, i, j):
    num_coords = set()
    for di in [-1, 0, +1]:
        for dj in [-1, 0, +1]:
            ni, nj = i + di, j + dj
            if (ni != i or nj != j) and 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj].isdigit():
                low_j, high_j = nj, nj
                while low_j >= 0 and grid[ni][low_j].isdigit():
                    low_j -= 1
                while high_j < len(grid[i]) and grid[ni][high_j].isdigit():
                    high_j += 1
                num_coords.add((ni, low_j + 1, high_j))
    return num_coords


def find_symbol_coords(grid, symbol_predicate):
    return ((i, j) for i in range(len(grid)) for j in range(len(grid[i])) if symbol_predicate(grid[i][j]))


def from_num_coords_to_num(num_coord):
    return int(grid[num_coord[0]][num_coord[1]:num_coord[2]])


def part1(grid):
    print(sum(map(from_num_coords_to_num,
                  reduce(set.union, map(lambda pos: find_adj_nums(grid, *pos),
                                        find_symbol_coords(grid,
                                                           symbol_predicate=lambda s: s != '.' and not s.isdigit()))))))


def part2(grid):
    print(sum(map(lambda adj_nums: int.__mul__(*map(from_num_coords_to_num, adj_nums)) if len(adj_nums) == 2 else 0,
                  map(lambda pos: find_adj_nums(grid, *pos),
                      find_symbol_coords(grid, symbol_predicate=lambda s: s == '*')))))


with open("input/day03.txt") as f:
    grid = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    part1(grid)
    part2(grid)
