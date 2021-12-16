def apply_commands(cmds, rules_for):
    lights = {}
    for cmd in cmds:
        cmd, (from_i, from_j), (to_i, to_j) = cmd
        for i in range(from_i, 1 + to_i):
            for j in range(from_j, 1 + to_j):
                lights[(i, j)] = rules_for(cmd, i, j, lights.get((i, j), 0))
    return sum(lights.values())


def part1(cmds):
    print(apply_commands(cmds,
                         rules_for=lambda cmd, i, j, v: 1 - v if cmd == 'toggle' else 1 if cmd == 'on' else 0))


def part2(cmds):
    print(apply_commands(cmds,
                         rules_for=lambda cmd, i, j, v: max(0,
                                                            v + (2 if cmd == 'toggle' else 1 if cmd == 'on' else -1))))


with open("input/day6.txt") as f:
    extract = lambda l: (l[-4], tuple(map(int, l[-3].split(','))), tuple(map(int, l[-1].split(','))))
    commands = list(map(lambda l: extract(l.replace('\n', '').split()), f.readlines()))
    part1(commands)
    part2(commands)
