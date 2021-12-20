def configurations():
    vx, vy, vz, sx, sy, sz = 0, 1, 2, 1, 1, 1
    for _ in range(4):
        for _ in range(4):
            yield vx, vy, vz, sx, sy, sz
            vx, vy, vz, sx, sy, sz = vz, vy, vx, sz, sy, -sx
        yield vy, vx, vz, sy, -sx, sz
        yield vy, vx, vz, -sy, sx, sz
        vx, vy, vz, sx, sy, sz = vx, vz, vy, sx, sz, -sy


def traslated_points_to_ref(ref_points, other_points):
    def diff(p1, p2):
        return tuple(c1 - c2 for c1, c2 in zip(p1, p2))

    for vx, vy, vz, sx, sy, sz in configurations():
        other_points_rotated = [(sx * op[vx], sy * op[vy], sz * op[vz]) for op in other_points]
        for ref_point in ref_points:
            for other_point in other_points_rotated:
                offset = diff(other_point, ref_point)
                c = {diff(other_point, offset) for other_point in other_points_rotated}
                if len(c & ref_points) >= 12:
                    return c, diff(ref_point, other_point)
    return set(), None


def fold_points(points_by_scanner):
    q, ref, scanners = points_by_scanner[1:], set(points_by_scanner[0]), [(0, 0, 0)]
    while q:
        others = q.pop(0)
        c, scanner = traslated_points_to_ref(ref, others)
        if c:
            ref |= c
            scanners.append(scanner)
        else:
            q.append(others)
    return ref, scanners


def part1(v):
    print(len(v))


def part2(scanners):
    def manhattan(p1, p2):
        return sum(map(lambda i: abs(p1[i] - p2[i]), range(len(p1))))

    print(max(manhattan(sp1, sp2) for sp1 in scanners for sp2 in scanners))


with open("input/day19.txt") as f:
    debug = True
    v = list(
        map(lambda l: list(map(lambda l: tuple(map(int, l.split(','))), l.split('\n')[1:])), f.read().split('\n\n')))
    ref_scanner_points, scanners = fold_points(v)
    part1(ref_scanner_points)
    part2(scanners)
