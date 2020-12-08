import intcode


def part1(program):
    program[1], program[2] = 12, 2
    intcode.execute(program, inputs=[], outputs=[])
    print(program[0])


def part2(program, expected_result):
    for noun in range(100):
        for verb in range(100):
            p = program[:]
            p[1], p[2] = noun, verb
            intcode.execute(p, inputs=[], outputs=[])
            if p[0] == expected_result:
                print(100 * noun + verb)


with open("day02.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v, expected_result=19690720)
