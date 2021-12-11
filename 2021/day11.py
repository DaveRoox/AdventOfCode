def step(g):
    to_flash = []
    for i in range(len(g)):
        for j in range(len(g[0])):
            g[i][j] += 1
            if g[i][j] == 10:
                to_flash.append((i, j))

    flashed, flashes = set(), 0
    while len(to_flash) > 0:
        i, j = to_flash.pop()
        flashed.add((i, j))
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < len(g)) or not (0 <= nj < len(g[0])) or (ni, nj) in flashed:
                    continue
                g[ni][nj] += 1
                if g[ni][nj] == 10:
                    to_flash.append((ni, nj))
        g[i][j] = 0
        flashes += 1

    return flashes


def part1(g):
    print(sum(step(g) for _ in range(100)))


def part2(g):
    steps = 1
    while step(g) != len(g) * len(g[0]):
        steps += 1
    print(steps)


with open("input/day11.txt") as f:
    g = list(map(lambda line: list(map(int, line.replace('\n', ''))), f.readlines()))
    part1([g[i][:] for i in range(len(g))])
    part2(g)
