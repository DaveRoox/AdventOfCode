from itertools import permutations


def execute(program, inputs, outputs, instr_ptr=0):
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

    n = len(program) - 1
    while instr_ptr <= n:
        op_code = program[instr_ptr] % 100
        par1_index = instr_ptr + 1 if program[instr_ptr] // 100 % 10 else program[min(n, instr_ptr + 1)]
        par2_index = instr_ptr + 2 if program[instr_ptr] // 1000 % 10 else program[min(n, instr_ptr + 2)]
        par3_index = instr_ptr + 3 if program[instr_ptr] // 10000 % 10 else program[min(n, instr_ptr + 3)]
        if op_code != 3 or len(inputs) > 0:
            instr_ptr = istr[op_code](par1_index, par2_index, par3_index, instr_ptr)
        else:
            break
    return instr_ptr  # returning the instruction pointer in order to restore the execution later


def part1(program):
    def evaluate_signal(phases):
        out = [0]
        for phase in phases:
            execute(program[:], inputs=[phase, out[-1]], outputs=out)
        return out[-1]

    print(max(map(evaluate_signal, permutations(range(5)))))


def part2(program):
    def evaluate_signal(phases):
        programs = [program[:] for _ in phases]
        instr_ptrs = [0 for _ in phases]
        inputs = [[phase] for phase in phases]
        inputs[0].append(0)

        i = 0
        while instr_ptrs[-1] < len(programs[-1]):
            next_i = (i + 1) % len(phases)
            instr_ptrs[i] = execute(programs[i], inputs[i], inputs[next_i], instr_ptrs[i])
            i = next_i

        return inputs[0][-1]

    print(max(map(evaluate_signal, permutations(range(5, 10)))))


with open("day07.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v)
    part2(v)
