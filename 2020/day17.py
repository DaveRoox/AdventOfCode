from functools import reduce


def count_active_3d(active, x, y, z):
    return sum(1
               for dx in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dz in (-1, 0, 1)
               if (x + dx, y + dy, z + dz) in active)


def count_active_4d(active, x, y, z, w):
    return sum(1
               for dx in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dz in (-1, 0, 1)
               for dw in (-1, 0, 1)
               if (x + dx, y + dy, z + dz, w + dw) in active)


def check_inactive_neighbors_3d(active, x, y, z):
    return set((x + dx, y + dy, z + dz)
               for dx in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dz in (-1, 0, 1)
               if (x + dx, y + dy, z + dz) not in active
               and count_active_3d(active, x + dx, y + dy, z + dz) == 3)


def check_inactive_neighbors_4d(active, x, y, z, w):
    return set((x + dx, y + dy, z + dz, w + dw)
               for dx in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dz in (-1, 0, 1)
               for dw in (-1, 0, 1)
               if (x + dx, y + dy, z + dz, w + dw) not in active
               and count_active_4d(active, x + dx, y + dy, z + dz, w + dw) == 3)


def step(active, ff1, ff2):
    s = set()
    for coords in active:
        if ff1(active, *coords) in (3, 4):
            s.add(coords)
        s = s.union(ff2(active, *coords))
    return s


def part1(g):
    print(len(reduce(lambda acc, _: step(acc, count_active_3d, check_inactive_neighbors_3d), range(6), g)))


def part2(g):
    print(len(reduce(lambda acc, _: step(acc, count_active_4d, check_inactive_neighbors_4d), range(6), g)))


with open("input/day17.txt") as f:
    v = [line.replace('\n', '') for line in f]
    v_3g = set((x, y, 0) for y in range(len(v)) for x in range(len(v[0])) if v[y][x] == '#')
    v_4g = set((x, y, z, 0) for x, y, z in v_3g)
    part1(v_3g)
    part2(v_4g)
