def run(program, inputs):
    p, i = 0, 0
    while p < len(program):
        op_code = program[p] % 100
        if op_code == 99:  # exit
            return
        first_operand = program[program[p + 1]] if (program[p] % 1000) // 100 == 0 else program[p + 1]
        if op_code == 3:  # input
            program[program[p + 1]] = inputs[i]
            p += 2
            i += 1  # next input, if any
        elif op_code == 4:  # output
            print(first_operand)
            p += 2
        else:
            second_operand = program[program[p + 2]] if (program[p] % 10000) // 1000 == 0 else program[p + 2]
            if op_code == 1:  # add
                program[program[p + 3]] = first_operand + second_operand
            elif op_code == 2:  # multiply
                program[program[p + 3]] = first_operand * second_operand
            elif op_code == 5:  # jump-if-true
                p = second_operand - 4 if first_operand != 0 else p - 1
            elif op_code == 6:  # jump-if-false
                p = second_operand - 4 if first_operand == 0 else p - 1
            elif op_code == 7:  # less-than
                program[program[p + 3]] = 1 if first_operand < second_operand else 0
            elif op_code == 8:  # equals
                program[program[p + 3]] = 1 if first_operand == second_operand else 0
            p += 4


with open('day05.txt') as f:
    original_program = list(map(int, f.readline().split(',')))
    run(original_program[:], inputs=[1])  # part 1
    run(original_program, inputs=[5])  # part 2
