def visit_points(points, from_coord, to_coord, with_dx, with_dy):
    x, y, x_end, y_end = *from_coord, *to_coord
    points[(x, y)] = 1 + points.get((x, y), 0)
    while x != x_end or y != y_end:
        x += with_dx
        y += with_dy
        points[(x, y)] = 1 + points.get((x, y), 0)


def sign(x):
    return 1 if x >= 0 else -1


def part1(coords):
    points = {}
    for coord in coords:
        x1, y1, x2, y2 = *coord[0], *coord[1]
        if x1 == x2:
            visit_points(points, from_coord=coord[0], to_coord=coord[1], with_dx=0, with_dy=sign(y2 - y1))
        elif y1 == y2:
            visit_points(points, from_coord=coord[0], to_coord=coord[1], with_dx=sign(x2 - x1), with_dy=0)

    print(sum(points[k] > 1 for k in points))


def part2(coords):
    points = {}
    for coord in coords:
        x1, y1, x2, y2 = *coord[0], *coord[1]
        if x1 == x2:
            visit_points(points, from_coord=coord[0], to_coord=coord[1], with_dx=0, with_dy=sign(y2 - y1))
        elif y1 == y2:
            visit_points(points, from_coord=coord[0], to_coord=coord[1], with_dx=sign(x2 - x1), with_dy=0)
        else:
            visit_points(points, from_coord=coord[0], to_coord=coord[1], with_dx=sign(x2 - x1), with_dy=sign(y2 - y1))

    print(sum(points[k] > 1 for k in points))


with open("input/day05.txt") as f:
    v = list(map(lambda l: list(map(lambda p: tuple(map(int, p.split(','))), l.split(' -> '))), f.readlines()))
    part1(v)
    part2(v)
