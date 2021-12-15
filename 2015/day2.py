def part1(v):
    print(sum(2 * sum((t[0] * t[1], t[1] * t[2], t[2] * t[0])) + min(t[0] * t[1], t[1] * t[2], t[2] * t[0]) for t in v))


def part2(v):
    print(sum(2 * (sum(t)-max(t)) + t[0]*t[1]*t[2] for t in v))


with open("input/day2.txt") as f:
    v = list(map(lambda l: tuple(map(int, l.replace('\n', '').split('x'))), f.readlines()))
    part1(v)
    part2(v)
