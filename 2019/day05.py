def execute(program, inputs):

    def get(inp):
        return inp.pop(0)

    def put(out, val):
        out.append(val)

    def _1(p1i, p2i, p3i, index):
        program[p3i] = program[p1i] + program[p2i]
        return index + 4

    def _2(p1i, p2i, p3i, index):
        program[p3i] = program[p1i] * program[p2i]
        return index + 4

    def _3(p1i, p2i, p3i, index):
        program[p1i] = get(inputs)
        return index + 2

    def _4(p1i, p2i, p3i, index):
        put(outputs, program[p1i])
        return index + 2

    def _5(p1i, p2i, p3i, index):
        return program[p2i] if program[p1i] != 0 else index + 3

    def _6(p1i, p2i, p3i, index):
        return program[p2i] if program[p1i] == 0 else index + 3

    def _7(p1i, p2i, p3i, index):
        program[p3i] = int(program[p1i] < program[p2i])
        return index + 4

    def _8(p1i, p2i, p3i, index):
        program[p3i] = int(program[p1i] == program[p2i])
        return index + 4

    def _99(p1i, p2i, p3i, index):
        return len(program)

    istr = {
        1: _1, 2: _2, 3: _3,
        4: _4, 5: _5, 6: _6,
        7: _7, 8: _8, 99: _99,
    }

    i, n, outputs = 0, len(program) - 1, []
    while i <= n:
        op_code = program[i] % 100
        par1_index = i + 1 if program[i] // 100 % 10 else program[min(n, i + 1)]
        par2_index = i + 2 if program[i] // 1000 % 10 else program[min(n, i + 2)]
        par3_index = i + 3 if program[i] // 10000 % 10 else program[min(n, i + 3)]
        i = istr[op_code](par1_index, par2_index, par3_index, i)

    return outputs[-1]


def part1(program):
    print(execute(program, inputs=[1]))


def part2(program):
    print(execute(program, inputs=[5]))


with open("day05.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v)
