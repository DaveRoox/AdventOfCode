from queue import PriorityQueue


def dijkstra(g):
    d, curr_cell = {(i, j): float('inf') for i in range(len(g)) for j in range(len(g[0]))}, (0, 0)
    d[curr_cell] = 0
    pq, visited = PriorityQueue(), set()
    pq.put((0, curr_cell))

    while not pq.empty():
        _, curr_cell = pq.get()
        visited.add(curr_cell)
        i, j = curr_cell
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            new_cell = (ni, nj)
            if 0 <= ni < len(g) and 0 <= nj < len(g[0]) and new_cell not in visited:
                old_cost, new_cost = d[new_cell], d[curr_cell] + g[ni][nj]
                if new_cost < old_cost:
                    pq.put((new_cost, new_cell))
                    d[new_cell] = new_cost

    return d[(len(g) - 1, len(g[0]) - 1)]


def part1(grid):
    print(dijkstra(grid))


def part2(grid):
    def new_value(i, j):
        def modulo(x):
            return x if x <= 9 else x - 9

        return modulo(grid[i % len(grid)][j % len(grid[0])] + i // len(grid) + j // len(grid[0]))

    print(dijkstra([[new_value(i, j) for j in range(5 * len(grid[0]))] for i in range(5 * len(grid))]))


with open("input/day15.txt") as f:
    g = list(map(lambda line: list(map(int, line.replace('\n', ''))), f.readlines()))
    part1(g)
    part2(g)
