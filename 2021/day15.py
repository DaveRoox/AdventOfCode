from queue import PriorityQueue


def dijkstra(rows, cols, value_for):
    distances, visited = {(0, 0): 0}, set()
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        _, curr_cell = pq.get()
        visited.add(curr_cell)
        i, j = curr_cell
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            new_cell = (ni, nj)
            if 0 <= ni < rows and 0 <= nj < cols and new_cell not in visited:
                old_cost, new_cost = distances.get(new_cell, float('inf')), distances[curr_cell] + value_for(ni, nj)
                if new_cost < old_cost:
                    pq.put((new_cost, new_cell))
                    distances[new_cell] = new_cost

    return distances[(rows - 1, cols - 1)]


def part1(grid):
    print(dijkstra(
        rows=len(grid),
        cols=len(grid[0]),
        value_for=lambda i, j: grid[i][j]))


def part2(grid):
    def modulo(x):
        return x if x <= 9 else x - 9

    print(dijkstra(
        rows=5 * len(grid),
        cols=5 * len(grid[0]),
        value_for=lambda i, j: modulo(grid[i % len(grid)][j % len(grid[0])] + i // len(grid) + j // len(grid[0]))))


with open("input/day15.txt") as f:
    g = list(map(lambda line: list(map(int, line.replace('\n', ''))), f.readlines()))
    part1(g)
    part2(g)
