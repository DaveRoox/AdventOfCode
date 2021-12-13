from functools import reduce


def fold(points, instruction):
    x_line, y_line = (int(instruction[1]), float('inf')) if instruction[0] == 'x' else (
        float('inf'), int(instruction[1]))
    return set((x if x <= x_line else 2 * x_line - x, y if y <= y_line else 2 * y_line - y) for x, y in points)


def part1(points, folds):
    print(len(fold(points, folds[0])))


def part2(points, folds):
    def print_points(points):
        min_x, max_x = min(p[0] for p in points), max(p[0] for p in points)
        min_y, max_y = min(p[1] for p in points), max(p[1] for p in points)
        for yy in range(min_y, 1 + max_y):
            for xx in range(min_x, 1 + max_x):
                print('#' if (xx, yy) in points else ' ', end='')
            print()

    print_points(reduce(lambda p, f: fold(p, f), folds, points))


with open("input/day13.txt") as f:
    v = [l.replace('\n', '') for l in f.readlines()]
    ii = v.index('')
    points = set(map(lambda s: tuple(map(int, s.split(','))), v[:ii]))
    folds = list(map(lambda s: tuple(s.split()[-1].split('=')), v[ii + 1:]))
    part1(points, folds)
    part2(points, folds)
