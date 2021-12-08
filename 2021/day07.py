def fuel_to_align(v, to_position, f):
    return sum(f(abs(p - to_position)) for p in v)


def part1(v):
    print(fuel_to_align(v,
                        to_position=sorted(v)[len(v) // 2],
                        f=lambda _: _))


def part2(v):
    d = 0.5 + sum(v) / len(v)
    print(fuel_to_align(v,
                        to_position=min(enumerate(sorted(v)), key=lambda x: abs(x[1] - d + x[0] / len(v)))[1],
                        f=lambda n: n * (n + 1) // 2))


with open("input/day07.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v)
    part2(v)
