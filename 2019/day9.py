def index(program, p, x, rel_base):
    v = 10 ** (x + 2)
    mode = (program[p] % v) // (v / 10)
    index = program[p + x] if mode == 0 else (p + x) if mode == 1 else (program[p + x] + rel_base)
    while len(program) <= index:
        program.append(0)
    return index


def run(program, inputs):
    p, i, rel_base = 0, 0, 0
    while p < len(program):
        op_code = program[p] % 100
        if op_code == 99:  # exit
            return
        first_index = index(program, p, 1, rel_base)
        if op_code == 3:  # input
            program[first_index] = inputs[i]
            p += 2
            i += 1  # next input, if any
        elif op_code == 4:  # output
            print(program[first_index])
            p += 2
        elif op_code == 9:  # change relative base
            rel_base += program[first_index]
            p += 2
        else: # two-parameter opcodes
            second_index = index(program, p, 2, rel_base)
            if op_code == 5:  # jump-if-true
                p = program[second_index] if program[first_index] != 0 else p + 3
            elif op_code == 6:  # jump-if-false
                p = program[second_index] if program[first_index] == 0 else p + 3
            else: # three-parameter opcodes
                third_index = index(program, p, 3, rel_base)
                if op_code == 1:  # add
                    program[third_index] = program[first_index] + program[second_index]
                elif op_code == 2:  # multiply
                    program[third_index] = program[first_index] * program[second_index]
                elif op_code == 7:  # less-than
                    program[third_index] = 1 if program[first_index] < program[second_index] else 0
                elif op_code == 8:  # equals
                    program[third_index] = 1 if program[first_index] == program[second_index] else 0
                p += 4


with open('./day9.txt') as f:
    original_program = list(map(int, f.readline().split(',')))
    run(original_program[:], inputs=[1])  # part 1
    run(original_program[:], inputs=[2])  # part 2
