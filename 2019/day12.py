import math
from functools import reduce


def sign(c1, c2):
    return 1 if c1 < c2 else -1 if c2 < c1 else 0


def lcm(a, b):
    return int((a * b) // math.gcd(a, b))


def step(pos, vel, n):
    for _ in range(n):
        for i in range(len(pos)):
            x1, y1, z1 = pos[i]
            for j in range(i + 1, len(pos)):
                x2, y2, z2 = pos[j]
                vel[i] = [vel[i][0] + sign(x1, x2), vel[i][1] + sign(y1, y2), vel[i][2] + sign(z1, z2)]
                vel[j] = [vel[j][0] + sign(x2, x1), vel[j][1] + sign(y2, y1), vel[j][2] + sign(z2, z1)]
            pos[i] = [x1 + vel[i][0], y1 + vel[i][1], z1 + vel[i][2]]
    return sum(sum(map(abs, p)) * sum(map(abs, v)) for p, v in zip(pos, vel))


def cycles(pos, vel, dim):  # calculates moons' period of positions and velocities for a given dimension (x, y or z)
    initial_state_pos, initial_state_vel = [p[dim] for p in pos], [v[dim] for v in vel]
    c = 0
    while c == 0 or initial_state_pos != [p[dim] for p in pos] or initial_state_vel != [v[dim] for v in vel]:
        for i in range(len(pos)):  # simulating a step for a single dimension only
            pi = pos[i][dim]
            for j in range(i + 1, len(pos)):
                s = sign(pi, pos[j][dim])
                vel[i][dim] += s
                vel[j][dim] -= s
            pos[i][dim] += vel[i][dim]
        c += 1
    return c


with open('./day12.txt') as f:
    positions = [
        list(map(int, list(dimension.split('=')[1] for dimension in line.replace('\n', '')[1:-1].split(', '))))
        for line in f
    ]
    velocities = [[0, 0, 0] for _ in range(len(positions))]
    print(step(positions[:], velocities[:], n=1000))  # part 1
    print(reduce(lambda acc, i: lcm(acc, cycles(positions[:], velocities[:], i)), range(3), 1))  # part 2
