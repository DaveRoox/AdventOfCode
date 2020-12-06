def part1(orbits):
    def count(obj):
        c = 0
        while obj != 'COM':
            obj = orbits[obj]
            c += 1
        return c

    print(sum(map(count, orbits)))


def part2(orbits):
    def path(obj):
        p = []
        while obj != 'COM':
            obj = orbits[obj]
            p.append(obj)
        return p

    p1, p2, k = path('YOU'), path('SAN'), 0
    while p1[-1 - k] == p2[-1 - k]:
        k += 1

    print(len(p1) + len(p2) - 2 * k)


with open("day06.txt") as f:
    o = dict(map(lambda s: s.split(')')[::-1], (line.replace('\n', '') for line in f)))
    part1(o)
    part2(o)
