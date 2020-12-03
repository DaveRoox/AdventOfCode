def traverse_with_slope(lines, dx, dy):
    x, y, trees = 0, 0, 0
    while y < len(lines):
        if lines[y][x] == '#':
            trees += 1
        x = (x + dx) % len(lines[0])
        y = y + dy
    return trees


def part1(lines):
    print(traverse_with_slope(lines, dx=3, dy=1))


def part2(lines):
    print(
        traverse_with_slope(lines, dx=1, dy=1) *
        traverse_with_slope(lines, dx=3, dy=1) *
        traverse_with_slope(lines, dx=5, dy=1) *
        traverse_with_slope(lines, dx=7, dy=1) *
        traverse_with_slope(lines, dx=1, dy=2)
    )


with open("day03.txt") as f:
    v = [line.replace('\n', '') for line in f]
    part1(v)
    part2(v)
