def part1(v):
    def is_nice(s):
        conditions = [
            lambda s: sum(s.count(c) for c in 'aeiou') >= 3,
            lambda s: any(x == y for x, y in zip(s, s[1:])),
            lambda s: all(x not in s for x in ('ab', 'cd', 'pq', 'xy')),
        ]
        return all(cond(s) for cond in conditions)
    print(sum(is_nice(s) for s in v))


def part2(v):
    def is_nice(s):
        conditions = [
            lambda s: any((x+y) in s and (x+y) in s[s.index(x+y)+2:] for x, y in zip(s, s[1:])),
            lambda s: any(x == y for x, y in zip(s, s[2:])),
        ]
        return all(cond(s) for cond in conditions)
    print(sum(is_nice(s) for s in v))


with open("input/day5.txt") as f:
    v = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    part1(v)
    part2(v)
