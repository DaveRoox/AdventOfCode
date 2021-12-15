def visited(instructions):
    x, y, v, movement = 0, 0, {(0, 0)}, {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    for cmd in instructions:
        mv_x, mv_y = movement[cmd]
        x += mv_x
        y += mv_y
        v.add((x, y))
    return v


def part1(instructions):
    print(len(visited(instructions)))


def part2(instructions):
    print(len(visited(instructions[::2]) | visited(instructions[1::2])))


with open("input/day3.txt") as f:
    v = f.readline().replace('\n', '')
    part1(v)
    part2(v)
