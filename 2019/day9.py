def run(program, inputs):
    p, i, rel_base = 0, 0, 0
    while p < len(program):
        op_code = program[p] % 100
        if op_code == 99:  # exit
            return
        first_mode = (program[p] % 1000) // 100
        first_index = program[p + 1] if first_mode == 0 else (p + 1) if first_mode == 1 else (program[p + 1] + rel_base)
        while len(program) <= first_index:
            program.append(0)
        first_operand = program[first_index]
        if op_code == 3:  # input
            program[first_index] = inputs[i]
            p += 2
            i += 1  # next input, if any
        elif op_code == 4:  # output
            print(first_operand)
            p += 2
        elif op_code == 9:  # change relative base
            rel_base += first_operand
            p += 2
        else:
            second_mode = (program[p] % 10000) // 1000
            second_index = program[p + 2] if second_mode == 0 else (p + 2) if second_mode == 1 else (program[p + 2] + rel_base)
            while len(program) <= second_index:
                program.append(0)
            second_operand = program[second_index]
            if op_code in (1, 2, 7, 8):
                third_mode = (program[p] % 100000) // 10000
                third_index = program[p + 3] if third_mode == 0 else (p + 3) if third_mode == 1 else (program[p + 3] + rel_base)
                while len(program) <= third_index:
                    program.append(0)
                if op_code == 1:  # add
                    program[third_index] = first_operand + second_operand
                elif op_code == 2:  # multiply
                    program[third_index] = first_operand * second_operand
                elif op_code == 7:  # less-than
                    program[third_index] = 1 if first_operand < second_operand else 0
                elif op_code == 8:  # equals
                    program[third_index] = 1 if first_operand == second_operand else 0
                p += 4
            elif op_code == 5:  # jump-if-true
                p = second_operand if first_operand != 0 else p + 3
            elif op_code == 6:  # jump-if-false
                p = second_operand if first_operand == 0 else p + 3


with open('./day9.txt') as f:
    original_program = list(map(int, f.readline().split(',')))
    run(original_program[:], inputs=[1])  # part 1
    run(original_program[:], inputs=[2])  # part 2
