def run(program, first_op, second_op):
    program[1:3] = [first_op, second_op]
    for i in range(0, len(program), 4):
        op_code = program[i]
        if op_code == 1:  # add
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
        elif op_code == 2:  # multiply
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
        elif op_code == 99:  # exit
            break
    return program[0]


def find_params(p):
    for noun in range(100):
        for verb in range(100):
            if run(p[:], first_op=noun, second_op=verb) == 19690720:
                return 100 * noun + verb


with open('./day2.txt') as f:
    original_program = list(map(int, f.readline().split(',')))
    print(run(original_program[:], first_op=12, second_op=2))  # part 1
    print(find_params(original_program))  # part 2
