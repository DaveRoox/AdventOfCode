def visited_points(segments, can_visit):
    points, sign = {}, lambda n: 1 if n > 0 else -1 if n < 0 else 0
    for segment in segments:
        if can_visit(segment):
            x, y, x_end, y_end = *segment[0], *segment[1]
            dx, dy = sign(x_end - x), sign(y_end - y)
            points[(x, y)] = 1 + points.get((x, y), 0)
            while x != x_end or y != y_end:
                x += dx
                y += dy
                points[(x, y)] = 1 + points.get((x, y), 0)
    return points


def part1(segments):
    print(sum(overlaps > 1 for overlaps in visited_points(segments,
                                                          can_visit=lambda s: s[0][0] == s[1][0] or s[0][1] == s[1][1]).values()))


def part2(segments):
    print(sum(overlaps > 1 for overlaps in visited_points(segments,
                                                          can_visit=lambda _: True).values()))


with open("input/day05.txt") as f:
    v = list(map(lambda l: list(map(lambda p: tuple(map(int, p.split(','))), l.split(' -> '))), f.readlines()))
    part1(v)
    part2(v)
