import threading

from aoc_utils import aoc_utils


def rows_match(r1, r2, vx, vy, vz, sign_x, sign_y, sign_z):
    sr2, count = {}, 0
    for p in r1:
        sr2[p] = 1 + sr2.get(p, 0)
    for p in r2:
        p = (sign_x * p[vx], sign_y * p[vy], sign_z * p[vz])
        if sr2.get(p, 0) > 0:
            count += 1
            if count >= min(12, len(r1)):
                return True
            sr2[p] -= 1
    return False


def can_overlap(m1, m2, vx, vy, vz, sx, sy, sz):
    return any(rows_match(r1, r2, vx, vy, vz, sx, sy, sz) for r1 in m1 for r2 in m2)


def overlaps(ref_points, other_points):
    ref_dist_matrix = get_distance_matrix(ref_points)
    other_dist_matrix = get_distance_matrix(other_points)
    for vx, vy, vz in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                for sz in [-1, 1]:
                    if can_overlap(ref_dist_matrix, other_dist_matrix, vx, vy, vz, sx, sy, sz):
                        return True
    return False


def get_scanner_position(ref_points, other_points):
    def overlapping(m1, m2, vx, vy, vz, sx, sy, sz):
        for i, row1 in enumerate(m1):
            for j, row2 in enumerate(m2):
                if rows_match(row1, row2, vx, vy, vz, sx, sy, sz):
                    return i, j
        return -1, -1

    ref_dist_matrix, other_dist_matrix = get_distance_matrix(ref_points), get_distance_matrix(other_points)
    for vx, vy, vz in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                for sz in [-1, 1]:
                    i, j = overlapping(ref_dist_matrix, other_dist_matrix, vx, vy, vz, sx, sy, sz)
                    if i >= 0 and j >= 0:
                        ref_point, other_point = ref_points[i], other_points[j]
                        scanner_position = (ref_point[0] - sx * other_point[vx],
                                            ref_point[1] - sy * other_point[vy],
                                            ref_point[2] - sz * other_point[vz])
                        return scanner_position, (vx, vy, vz), (sx, sy, sz)
    return None, (0, 1, 2), (1, 1, 1)


def get_distance_matrix(points):
    def diff(p1, p2):
        return tuple(map(lambda i: p1[i] - p2[i], range(len(p1))))

    return [[diff(point1, point2) for point2 in points] for point1 in points]


def points_relative_to_ref(ref_points, other_points):
    scanner_position, (vx, vy, vz), (sx, sy, sz) = get_scanner_position(ref_points, other_points)
    if scanner_position is None:
        return set(), None, (vx, vy, vz), (sx, sy, sz)
    return set(map(lambda op: (scanner_position[0] + sx * op[vx],
                               scanner_position[1] + sy * op[vy],
                               scanner_position[2] + sz * op[vz]), other_points)), scanner_position, (vx, vy, vz), (
               sx, sy, sz)


def find_overlapping_for(v, mapping, i):
    for j in range(i + 1, len(v)):
        if overlaps(v[i], v[j]):
            if i not in mapping:
                mapping[i] = []
            mapping[i].append(j)
            if j not in mapping:
                mapping[j] = []
            mapping[j].append(i)
            if debug:
                print('overlapping: {0} <-> {1} '.format(i, j))


def visit_optimized(v, key, mapping, visited, results):
    threads, subresults = [], []
    for adj in mapping[key]:
        if adj not in visited:
            visited.add(adj)
            if debug:
                print('spawning thread to visit {} from {}...'.format(adj, key))
            threads.append(threading.Thread(target=visit_optimized, args=(v, adj, mapping, visited, subresults)))
            threads[-1].start()
    for t in threads:
        t.join()
    ref, key_scanners = set(v[key]), []
    for adj, adj_relative_scanners in subresults:
        new_points, adj_scanner, (vx, vy, vz), (sx, sy, sz) = points_relative_to_ref(v[key], v[adj])
        ref = ref.union(new_points)
        key_scanners.append(adj_scanner)
        for sc in adj_relative_scanners:
            key_scanners.append(
                (adj_scanner[0] + sx * sc[vx], adj_scanner[1] + sy * sc[vy], adj_scanner[2] + sz * sc[vz]))
    v[key] = list(ref)
    results.append((key, key_scanners))


def aggregate_all_points(v):
    mapping, threads = {}, []

    # bulding the graph
    for i in range(len(v)):
        t = threading.Thread(target=find_overlapping_for, args=(v, mapping, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    if debug:
        print(mapping)

    result = []
    # DFS-like inspection
    visit_optimized(v, 0, mapping, {0}, result)
    return v[0], result[0][1]


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
    ref_scanner_points, scanners = aggregate_all_points(v)
    part1(ref_scanner_points)
    part2(scanners)
