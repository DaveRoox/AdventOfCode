def part1(groups):
    print(sum(len({*''.join(g)}) for g in groups))


def part2(groups):
    r = 0
    for g in groups:
        m = {}
        for l in ''.join(g):
            if l not in m:
                m[l] = 0
            m[l] += 1
        r += list(m.values()).count(len(g))
    print(r)


with open("input/day06.txt") as f:
    ans = [line.replace('\n', '') for line in f]
    groups, group = [], []
    for a in ans:
        if not a:  # switching group
            groups.append(group)
            group = []
        else:
            group.append(a)
    groups.append(group)
    part1(groups)
    part2(groups)
