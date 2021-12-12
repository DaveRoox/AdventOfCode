def dfs(curr, end, caves, bonus_condition, seen, has_two=False):
    if curr == end:
        return 1
    r = 0
    for cave in caves[curr]:
        if cave.isupper():
            r += dfs(cave, end, caves, bonus_condition, seen, has_two)
        elif seen.get(cave, 0) == 0 or bonus_condition(seen[cave], has_two):
            seen[cave] = seen.get(cave, 0) + 1
            r += dfs(cave, end, caves, bonus_condition, seen, has_two or seen[cave] == 2)
            seen[cave] -= 1
    return r


def part1(graph):
    print(dfs('start', 'end', graph, bonus_condition=lambda _, __: False, seen={}))


def part2(graph):
    print(dfs('start', 'end', graph, bonus_condition=lambda n, has_two: n == 1 and not has_two, seen={}))


with open("input/day12.txt") as f:
    g = list(map(lambda l: tuple(l.replace('\n', '').split('-')), f.readlines()))
    caves_adj = {}
    for k, v in g:
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
