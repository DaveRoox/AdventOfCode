def dfs(curr, end, caves, max, is_ok, seen={}, has_max=False):
    if curr == end:
        return 1
    r = 0
    for cave in caves[curr]:
        n = seen.get(cave, 0)
        if cave.isupper():
            r += dfs(cave, end, caves, max, is_ok, seen, has_max)
        elif n < max and is_ok(not has_max or n != max - 1):
            seen[cave] = n + 1
            r += dfs(cave, end, caves, max, is_ok, seen, has_max or seen[cave] == max)
            seen[cave] -= 1
    return r


def part1(graph):
    print(dfs('start', 'end', graph, max=1, is_ok=lambda _: True))


def part2(graph):
    print(dfs('start', 'end', graph, max=2, is_ok=lambda _: _))


with open("input/day12.txt") as f:
    caves_adj = {}
    for k, v in list(map(lambda l: tuple(l.replace('\n', '').split('-')), f.readlines())):
        if v != 'start':  # we don't want to visit 'start' multiple times, so we can avoid storing it as adjacent
            if k not in caves_adj:
                caves_adj[k] = []
            caves_adj[k].append(v)
        if k != 'start':  # same
            if v not in caves_adj:
                caves_adj[v] = []
            caves_adj[v].append(k)
    part1(caves_adj)
    part2(caves_adj)
