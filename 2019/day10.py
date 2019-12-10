import math
from functools import reduce


def get_asteroids(grid):
    result = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                result.append((x, y))
    return result


def alpha(p1, p2):  # clockwise angle in radians between p1 and p2. y grows from top to bottom.
    return (2.5 * math.pi - math.atan2(p1[1] - p2[1], p2[0] - p1[0])) % (2 * math.pi)


def visible_asteroids(p, asteroids):
    return len(set(map(lambda a: alpha(p, a), asteroids)))


def append(accumulator, p, asteroid):
    angle = alpha(p, asteroid)
    if angle not in accumulator:
        accumulator[angle] = [[], 0]
    accumulator[angle][0].append(asteroid)
    return accumulator


def polverize(p, asteroids, n):
    # for each angle, it has the list of points sorted by distance from p
    angles_map = reduce(lambda acc, asteroid: append(acc, p, asteroid), asteroids, {})
    for angle in angles_map:
        angles_map[angle][0].sort(key=lambda a: abs(p[0] - a[0]) + abs(p[1] - a[1]))  # sorting by ascending distance

    i, angles = -1, sorted(angles_map.keys())
    while n > 0:
        i = (i + 1) % len(angles)
        l, index = angles_map[angles[i]]
        if index < len(l):  # "consuming" the nearest asteroid from the first non-empty list on the successive angle
            angles_map[angles[i]][1] = index + 1  # index of "polverized" asteroids in that list
            n -= 1

    l, index = angles_map[angles[i]]
    x, y = l[index - 1]
    return 100 * x + y


with open('./day10.txt') as f:
    asteroids = get_asteroids([line.replace('\n', '') for line in f.readlines()])
    p, count = max(map(lambda a: (a, visible_asteroids(a, asteroids)), asteroids), key=lambda t: t[1])
    print(count)  # part 1
    print(polverize(p, asteroids, n=200))  # part 2
