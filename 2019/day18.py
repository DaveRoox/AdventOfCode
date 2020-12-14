import math


def find_position(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == '@':
                return i, j


def find_min_path_distance(g, src, dst, visited):
    if src == dst:
        return 0, set()

    visited.add(src)
    min_sub_path_length, keys_to_collect = math.inf, None
    for i, j in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
        ni, nj = src[0] + i, src[1] + j
        if 0 <= ni < len(g) and 0 <= nj < len(g[0]) and (ni, nj) not in visited:
            c = g[ni][nj]
            if c != '#':
                sub_path_length, sub_keys_to_collect = find_min_path_distance(g, (ni, nj), dst, visited)
                if sub_path_length < min_sub_path_length:
                    min_sub_path_length = sub_path_length
                    keys_to_collect = sub_keys_to_collect
                    if c.isalpha() and c.isupper():
                        keys_to_collect.add(c.lower())
    visited.remove(src)
    return 1 + min_sub_path_length, keys_to_collect


def find_distances(g, pos, keys):
    distances = {}
    for key in keys:
        if pos != key:
            p, needed_keys = find_min_path_distance(g, pos, key, visited=set())
            if p < math.inf:
                distances[g[key[0]][key[1]]] = (p, needed_keys)
    return distances


def ggg(g, pos, distances, collected_keys):
    if len(collected_keys) == len(distances):
        return 0
    collected_keys.add(pos)
    min_distance = math.inf
    for key in distances[pos]:
        d, needed_keys = distances[pos][key]
        if key not in collected_keys and all(k in collected_keys for k in needed_keys):
            min_distance = min(min_distance, d + ggg(g, key, distances, collected_keys))
    collected_keys.remove(pos)
    return 1 + min_distance


def part1(grid):
    keys = set((i, j) for j in range(len(grid[0])) for i in range(len(grid)) if g[i][j].islower())
    distances = {g[key[0]][key[1]]: find_distances(g, key, keys) for key in keys}
    distances['@'] = find_distances(g, find_position(grid), keys)
    res = ggg(grid, '@', distances, collected_keys=set())
    print(res)


def part2(numbers):
    pass


with open("input/day18.txt") as f:
    g = [line.replace('\n', '') for line in f]
    part1(g)
    part2(g)
