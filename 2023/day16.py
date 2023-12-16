def cmp(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def move(grid, i, j, prev_i, prev_j, visited, loop_detection):
    while 0 <= i < len(grid) and 0 <= j < len(grid[i]) and (i, j, prev_i, prev_j) not in loop_detection:
        loop_detection.add((i, j, prev_i, prev_j))
        visited.add((i, j))
        cell, new_i, new_j = grid[i][j], i, j
        if cell == '.':
            new_i, new_j = 2 * i - prev_i, 2 * j - prev_j
        if cell == '/':
            new_i, new_j = i + cmp(prev_j, j), j + cmp(prev_i, i)
        if cell == '\\':
            new_i, new_j = i + cmp(j, prev_j), j + cmp(i, prev_i)
        if cell == '|':
            if prev_j != j:
                move(grid, i - 1, j, i, j, visited, loop_detection)
                move(grid, i + 1, j, i, j, visited, loop_detection)
                return
            new_i = 2 * i - prev_i
        if cell == '-':
            if prev_i != i:
                move(grid, i, j - 1, i, j, visited, loop_detection)
                move(grid, i, j + 1, i, j, visited, loop_detection)
                return
            new_j = 2 * j - prev_j
        i, j, prev_i, prev_j = new_i, new_j, i, j


def count_moves(grid, i, j, prev_i, prev_j):
    visited = set()
    move(grid, i, j, prev_i, prev_j, visited, loop_detection=set())
    return len(visited)


def part1(grid):
    print(count_moves(grid, 0, 0, 0, -1))


def part2(lines):
    # max tiles going downwards
    downwards_max = max(count_moves(grid, i=0, j=j, prev_i=-1, prev_j=j) for j in range(len(grid[0])))
    # max tiles going upwards
    upwards_max = max(count_moves(grid, i=len(grid) - 1, j=j, prev_i=len(grid), prev_j=j) for j in range(len(grid[0])))
    # max tiles going rightwards
    rightwards_max = max(count_moves(grid, i=i, j=0, prev_i=i, prev_j=-1) for i in range(len(grid)))
    # max tiles going leftwards
    leftwards_max = max(
        count_moves(grid, i=i, j=len(grid[0]) - 1, prev_i=i, prev_j=len(grid[0])) for i in range(len(grid)))
    print(max(downwards_max, upwards_max, rightwards_max, leftwards_max))


with open("input/day16.txt") as f:
    grid = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    part1(grid)
    part2(grid)
