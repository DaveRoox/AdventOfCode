from functools import reduce


def part1(g):
    def is_lowest_point(g, i, j):
        return all(g[i][j] < g[i + di][j + dj] for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)] if
                   0 <= i + di < len(g) and 0 <= j + dj < len(g[0]))

    print(sum(1 + g[i][j] for i in range(len(g)) for j in range(len(g[0])) if is_lowest_point(g, i, j)))


def part2(g):
    def expand(g, i, j, visited):
        if not (0 <= i < len(g)) or not (0 <= j < len(g[0])) or g[i][j] == 9 or (i, j) in visited:
            return 0
        visited.add((i, j))
        r = 1
        r += expand(g, i - 1, j, visited)
        r += expand(g, i + 1, j, visited)
        r += expand(g, i, j - 1, visited)
        r += expand(g, i, j + 1, visited)
        return r

    visited = set()
    basins = [expand(g, i, j, visited) for i in range(len(g)) for j in range(len(g[0])) if (i, j) not in visited]
    print(reduce(int.__mul__, sorted(basins)[-3:], 1))


with open("input/day09.txt") as f:
    g = list(map(lambda line: list(map(int, line.replace('\n', ''))), f.readlines()))
    part1(g)
    part2(g)
