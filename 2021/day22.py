def intersection(cube1, cube2):
    (x1min, x1max), (y1min, y1max), (z1min, z1max) = cube1
    (x2min, x2max), (y2min, y2max), (z2min, z2max) = cube2
    if x1max < x2min or x2max < x1min or y1max < y2min or y2max < y1min or z1max < z2min or z2max < z1min:
        return set()
    return {((max(x1min, x2min), min(x1max, x2max)),
             (max(y1min, y2min), min(y1max, y2max)),
             (max(z1min, z2min), min(z1max, z2max)))}


def subtraction(cube1, cube2):
    (x1min, x1max), (y1min, y1max), (z1min, z1max) = cube1
    intersect = intersection(cube1, cube2)
    if not intersect:
        return {cube1}
    (x3min, x3max), (y3min, y3max), (z3min, z3max) = intersect.pop()
    s = set()
    if x1min < x3min:
        s.add(((x1min, x3min - 1), (y1min, y1max), (z1min, z1max)))
    if x3max < x1max:
        s.add(((x3max + 1, x1max), (y1min, y1max), (z1min, z1max)))
    if y1min < y3min:
        s.add(((x1min, x1max), (y1min, y3min - 1), (z1min, z1max)))
    if y3max < y1max:
        s.add(((x1min, x1max), (y3max + 1, y1max), (z1min, z1max)))
    if z1min < z3min:
        s.add(((x1min, x1max), (y1min, y1max), (z1min, z3min - 1)))
    if z3max < z1max:
        s.add(((x1min, x1max), (y1min, y1max), (z3max + 1, z1max)))
    return s


def fold(folded_cubes, new_cubes):
    while new_cubes:
        new_cube = new_cubes.pop(0)
        for folded_cube in folded_cubes:
            intersect = intersection(folded_cube, new_cube)
            if intersect:
                new_cubes = list(subtraction(new_cube, intersect.pop())) + new_cubes
                break
        else:
            folded_cubes.add(new_cube)
    return folded_cubes


def apply_commands(cubes):
    on = set()
    for cmd, cube in cubes:
        if cmd == 'on':
            on = fold(on, [cube])
        else:
            on = fold(set(), sum((list(subtraction(c, cube)) for c in on), []))
    return sum((xmax - xmin + 1) * (ymax - ymin + 1) * (zmax - zmin + 1)
               for (xmin, xmax), (ymin, ymax), (zmin, zmax) in on)


def part1(cubes):
    cubes = list(filter(lambda cube: -50 <= cube[1][0][0] and cube[1][0][1] <= 50 and
                                     -50 <= cube[1][1][0] and cube[1][1][1] <= 50 and
                                     -50 <= cube[1][2][0] and cube[1][2][1] <= 50, cubes))
    print(apply_commands(cubes))


def part2(cubes):
    print(apply_commands(cubes))


with open("input/day22.txt") as f:
    v = []
    for line in f.readlines():
        cmd, cubes = line.replace('\n', '').split()
        v.append((cmd, tuple(tuple(map(int, cube.split('=')[1].split('..'))) for cube in cubes.split(','))))
    part1(v)
    part2(v)
