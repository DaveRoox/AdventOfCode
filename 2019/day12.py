import math
from functools import reduce


def sign(c1, c2):
    return 1 if c1 < c2 else -1 if c2 < c1 else 0


def lcm(a, b):
    return a * b // math.gcd(a, b)


def step(pos, vel):
    for i in range(len(pos)):
        x1, y1, z1 = pos[i]
        for j in range(i + 1, len(pos)):
            x2, y2, z2 = pos[j]
            vel[i] = [vel[i][0] + sign(x1, x2), vel[i][1] + sign(y1, y2), vel[i][2] + sign(z1, z2)]
            vel[j] = [vel[j][0] + sign(x2, x1), vel[j][1] + sign(y2, y1), vel[j][2] + sign(z2, z1)]
        pos[i] = [x1 + vel[i][0], y1 + vel[i][1], z1 + vel[i][2]]


def cycles(pos, vel, coordinate_index):
    initial_pos = [p.copy() for p in pos]
    initial_vel = [v.copy() for v in vel]
    c = 0
    while True:
        for i in range(len(pos)):
            d1 = pos[i][coordinate_index]
            for j in range(i + 1, len(pos)):
                d2 = pos[j][coordinate_index]
                vel[i][coordinate_index] += sign(d1, d2)
                vel[j][coordinate_index] += sign(d2, d1)
            pos[i][coordinate_index] += vel[i][coordinate_index]
        c += 1
        if pos == initial_pos and vel == initial_vel:
            break
    return c


def part1(pos):
    vel = [[0, 0, 0] for i in range(len(pos))]
    n = 1000
    while n > 0:
        step(pos, vel)
        n -= 1
    print(sum(sum(map(abs, p)) * sum(map(abs, v)) for p, v in zip(pos, vel)))


def part2(pos):
    print(reduce(lambda acc, i: lcm(acc, cycles(pos, [[0, 0, 0] for _ in range(len(pos))], i)), range(3), 1))


with open("input/day12.txt") as f:
    m = list(
        map(lambda l: list(map(lambda c: int(c.split('=')[1]), l.split(', '))), (l.replace('\n', '')[1:-1] for l in f))
    )
    part1(m[:])
    part2(m)
