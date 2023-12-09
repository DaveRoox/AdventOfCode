def diffs(v):
    d, last = [v], v
    while any(last):
        last = [x2 - x1 for x1, x2 in zip(last, last[1:])]
        d.append(last)
    return d


def reconstruct(v):
    d = diffs(v)
    for i in range(len(d) - 2, -1, -1):
        pre, post = d[i][0] - d[i + 1][0], d[i][-1] + d[i + 1][-1]
        d[i] = [pre] + d[i]
        d[i].append(post)
    return d[0]


def part1(values):
    print(sum(reconstruct(v)[-1] for v in values))


def part2(values):
    print(sum(reconstruct(v)[0] for v in values))


with open("input/day09.txt") as f:
    values = list(map(lambda l: list(map(int, l.replace('\n', '').split())), f.readlines()))
    part1(values)
    part2(values)
