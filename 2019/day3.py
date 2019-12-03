def read_path(f):
    last_x, last_y = 0, 0
    movements = [(last_x, last_y)]
    for move in f.readline().split(','):
        dir, ampl = move[0], int(move[1:])
        if dir in ('U', 'D'):
            last_y += ampl if dir == 'U' else -ampl
        else:
            last_x += ampl if dir == 'R' else -ampl
        movements.append((last_x, last_y))
    return movements


def find_cross_points(w1, w2):
    cross_points = []
    for (x1prev, y1prev), (x1, y1) in zip(w1, w1[1:]):
        is_horizontal1 = y1 == y1prev
        for (x2prev, y2prev), (x2, y2) in zip(w2, w2[1:]):
            is_horizontal2 = y2 == y2prev
            if is_horizontal1 == is_horizontal2:  # the wires are parallel
                continue
            if is_horizontal1:  # wire2 is vertical
                y = y1
                ymin, ymax = min(y2prev, y2), max(y2prev, y2)
                x = x2
                xmin, xmax = min(x1prev, x1), max(x1prev, x1)
            else:  # wire1 is vertical
                y = y2
                ymin, ymax = min(y1prev, y1), max(y1prev, y1)
                x = x1
                xmin, xmax = min(x2prev, x2), max(x2prev, x2)
            if xmin < x < xmax and ymin < y < ymax:
                cross_points.append((x, y))
    return cross_points


def walking_distance(target_point, movements):
    x, y, m, steps = 0, 0, 0, 0
    target_x, target_y = target_point[0], target_point[1]
    while x != target_x or y != target_y:
        new_x, new_y = movements[m]
        if new_x != x:
            dy = 0
            dx = 1 if new_x > x else -1
        else:  # new_y != y
            dx = 0
            dy = 1 if new_y > y else -1
        while (x != target_x or y != target_y) and (x != new_x or y != new_y):
            x += dx
            y += dy
            steps += 1
        m += 1
    return steps


with open('./day3.txt') as f:
    w1 = read_path(f)
    w2 = read_path(f)
    cross_points = find_cross_points(w1, w2)
    print(min(map(lambda p: abs(p[0]) + abs(p[1]), cross_points)))  # part 1
    print(min(map(lambda p: walking_distance(p, w1) + walking_distance(p, w2), cross_points)))  # part 2
