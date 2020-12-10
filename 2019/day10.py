import math


def get_asteroids(grid):
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                positions.append((j, i))
    return positions


def alpha(p1, p2):  # clockwise angle in radians between p1 and p2. y grows from top to bottom.
    return (2.5 * math.pi - math.atan2(p1[1] - p2[1], p2[0] - p1[0])) % (2 * math.pi)


def visible_asteroids(p, asteroids):
    return len(set(map(lambda a: alpha(p, a), asteroids)))


def part1(grid):
    asteroids = get_asteroids(grid)
    print(max(map(lambda a: visible_asteroids(a, asteroids), asteroids)))


def part2(grid):
    def group_asteroids_by_angle_sorted_by_distance_from(p):
        m = {}
        for a in asteroids:
            if a != p:
                angle = alpha(p, a)
                if angle not in m:
                    m[angle] = [[], 0]
                m[angle][0].append(a)
        for angle in m:
            m[angle][0].sort(key=lambda a: abs(a[0] - p[0]) + abs(a[1] - p[1]))
        return m

    def get_kth_asteroid(m, k):
        i, angles = 0, sorted(m.keys())
        while k > 0:
            angle = angles[i]
            if m[angle][1] < len(m[angle][0]):
                m[angle][1] += 1
                k -= 1
                if k == 0:
                    return m[angle][0][m[angle][1] - 1]
            i = (i + 1) % len(angles)

    asteroids = get_asteroids(grid)
    p = max(asteroids, key=lambda a: visible_asteroids(a, asteroids))
    _200th_asteroid = get_kth_asteroid(group_asteroids_by_angle_sorted_by_distance_from(p), k=200)
    print(100 * _200th_asteroid[0] + _200th_asteroid[1])


with open("input/day10.txt") as f:
    g = [list(line.replace('\n', '')) for line in f]
    part1(g)
    part2(g)
