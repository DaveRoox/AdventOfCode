from queue import PriorityQueue


def dijkstra(g):
    d = {(i, j): float('inf') for i in range(len(g)) for j in range(len(g[0]))}
    d[(0, 0)] = 0
    pq, visited = PriorityQueue(), set()
    pq.put((0, (0, 0)))

    while not pq.empty():
        _, curr_cell = pq.get()
        visited.add(curr_cell)
        i, j = curr_cell
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            new_cell = (ni, nj)
            if 0 <= ni < len(g) and 0 <= nj < len(g[0]) and new_cell not in visited:
                old_cost = d[new_cell]
                new_cost = d[curr_cell] + g[ni][nj]
                if new_cost < old_cost:
                    pq.put((new_cost, new_cell))
                    d[new_cell] = new_cost

    return d[(len(g) - 1, len(g[0]) - 1)]


def part1(grid):
    print(dijkstra(grid))


def part2(grid):
    new_grid = [[0 for _ in range(5 * len(g[0]))] for _ in range(5 * len(g))]
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if i < len(grid) and j < len(grid[0]):
                new_grid[i][j] = grid[i][j]
            elif i < len(grid):
                new_grid[i][j] = new_grid[i][j - len(grid[0])] + 1
            else:
                new_grid[i][j] = new_grid[i - len(grid)][j] + 1
            if new_grid[i][j] == 10:
                new_grid[i][j] = 1
    print(dijkstra(new_grid))


with open("input/day15.txt") as f:
    g = list(map(lambda line: list(map(int, line.replace('\n', ''))), f.readlines()))
    part1(g)
    part2(g)
