def part1(commands):

    def forward(n):
        nonlocal hor
        hor += n

    def up(n):
        nonlocal depth
        depth -= n

    def down(n):
        nonlocal depth
        depth += n

    depth, hor = 0, 0
    m = {
        'forward': forward,
        'up': up,
        'down': down,
    }
    for command in commands:
        m[command[0]](int(command[1]))
    print(hor * depth)


def part2(commands):

    def forward(n):
        nonlocal hor, depth
        hor += n
        depth += aim * n

    def up(n):
        nonlocal aim
        aim -= n

    def down(n):
        nonlocal aim
        aim += n

    aim, depth, hor = 0, 0, 0
    m = {
        'forward': forward,
        'up': up,
        'down': down,
    }
    for command in commands:
        m[command[0]](int(command[1]))
    print(hor * depth)


with open("input/day02.txt") as f:
    v = list(map(lambda l: l.split(), f.readlines()))
    part1(v)
    part2(v)
