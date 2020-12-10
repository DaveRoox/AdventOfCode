import intcode


def part1(program):
    out = []
    intcode.execute(program, inputs=[], outputs=out)
    print(out[2::3].count(2))


def part2(program):
    def find_symbol(s):
        for i in range(len(out) - 3, -1, -3):
            x, _, value = out[i], out[i + 1], out[i + 2]
            if value == s:
                return x

    def get_score():
        for i in range(len(out) - 3, -1, -3):
            x, y, value = out[i], out[i + 1], out[i + 2]
            if x == -1 and y == 0:
                return value

    program[0] = 2
    instr_ptr, rel_ptr, inp, out = 0, 0, [0], []
    while instr_ptr < len(program):
        out = []
        instr_ptr, rel_ptr = intcode.execute(program, inputs=inp, outputs=out)
        user_x, ball_x = find_symbol(3), find_symbol(4)
        inp.append(0 if user_x == ball_x else 1 if user_x < ball_x else -1)
    print(get_score())


with open("input/day13.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v)
