def part1(movements):
    y, x = 0, 0
    positions = {(y, x)}
    for r, c in movements:
        y += r
        x += c
        positions.add((y, x))
    return len(positions)


def part2(movements):
    y1, x1 = 0, 0
    y2, x2 = 0, 0
    positions = {(0, 0)}
    for (r1, c1), (r2, c2) in zip(movements[::2], movements[1::2]):
        y1 += r1
        x1 += c1
        positions.add((y1, x1))
        y2 += r2
        x2 += c2
        positions.add((y2, x2))
    if len(movements) % 2 == 1:
        r1, c1 = movements[-1]
        positions.add((y1 + r1, x1 + c1))
    return len(positions)


with open('./day3.txt') as f:
    dirs = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    movements = [dirs[m] for m in f.readline()]
    print(part1(movements))  # part 1
    print(part2(movements))  # part 2
