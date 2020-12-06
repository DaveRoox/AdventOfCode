def execute(program):
    i = 0
    while i < len(program):
        if program[i] is 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            i += 4
        elif program[i] is 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
            i += 4
        elif program[i] is 99:
            i = len(program)
    return program[0]


def part1(program):
    program[1], program[2] = 12, 2
    print(execute(program))


def part2(program, expected_result):
    for noun in range(100):
        for verb in range(100):
            p = program[:]
            p[1], p[2] = noun, verb
            if execute(p) == expected_result:
                print(100 * noun + verb)


with open("day02.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v, expected_result=19690720)
