from functools import reduce


def fold(points, instruction):
    def max_x():
        return max(points, key=lambda p: p[0])[0]

    def max_y():
        return max(points, key=lambda p: p[1])[1]

    x_line, y_line = (int(instruction[1]), max_y()) if instruction[0] == 'x' else (max_x(), int(instruction[1]))
    return set((x if x <= x_line else 2 * x_line - x, y if y <= y_line else 2 * y_line - y) for x, y in points)


def part1(points, folds):
    print(len(fold(points, folds[0])))


def part2(points, folds):
    def print_points(points):
        min_x, max_x = min(points, key=lambda p: p[0])[0], max(points, key=lambda p: p[0])[0]
        min_y, max_y = min(points, key=lambda p: p[1])[1], max(points, key=lambda p: p[1])[1]
        for yy in range(min_y, 1 + max_y):
            for xx in range(min_x, 1 + max_x):
                print('#' if (xx, yy) in points else '.', end='')
            print()

    print_points(reduce(lambda p, f: fold(p, f), folds, points))


with open("input/day13.txt") as f:
    v = [l.replace('\n', '') for l in f.readlines()]
    ii = v.index('')
    points = set(map(lambda s: tuple(map(int, s.split(','))), v[:ii]))
    folds = list(map(lambda s: tuple(s.split()[-1].split('=')), v[ii + 1:]))
    part1(points, folds)
    part2(points, folds)
