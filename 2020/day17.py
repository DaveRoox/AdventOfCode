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


def step_3d(active):
    s = set()
    min_x, max_x = min(p[0] for p in active), max(p[0] for p in active)
    min_y, max_y = min(p[1] for p in active), max(p[1] for p in active)
    min_z, max_z = min(p[2] for p in active), max(p[2] for p in active)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                pos = (x, y, z)
                active_neigh = count_active_3d(active, *pos)
                if pos in active and active_neigh in (3, 4) or pos not in active and active_neigh == 3:
                    s.add(pos)
    return s


def step_4d(active):
    s = set()
    min_x, max_x = min(p[0] for p in active), max(p[0] for p in active)
    min_y, max_y = min(p[1] for p in active), max(p[1] for p in active)
    min_z, max_z = min(p[2] for p in active), max(p[2] for p in active)
    min_w, max_w = min(p[3] for p in active), max(p[3] for p in active)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    pos = (x, y, z, w)
                    active_neigh = count_active_4d(active, *pos)
                    if pos in active and active_neigh in (3, 4) or pos not in active and active_neigh == 3:
                        s.add(pos)
    return s


def part1(g):
    print(len(reduce(lambda acc, _: step_3d(acc), range(6), g)))


def part2(g):
    print(len(reduce(lambda acc, _: step_4d(acc), range(6), g)))


with open("input/day17.txt") as f:
    v = [line.replace('\n', '') for line in f]
    v_3g = set((x, y, 0) for y in range(len(v)) for x in range(len(v[0])) if v[y][x] == '#')
    v_4g = set((x, y, z, 0) for x, y, z in v_3g)
    part1(v_3g)
    part2(v_4g)
