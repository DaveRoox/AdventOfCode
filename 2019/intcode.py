def execute(program, inputs, outputs, instr_ptr=0, rel_ptr=0):
    def get(inp):
        return inp.pop(0)

    def put(out, val):
        out.append(val)

    def extend_memory_if_necessary(location):
        if location >= len(program):
            program.extend([0] * (location - len(program) + 1))

    def _1(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(max(p1i, p2i, p3i))
        program[p3i] = program[p1i] + program[p2i]
        return index + 4, relative_index

    def _2(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(max(p1i, p2i, p3i))
        program[p3i] = program[p1i] * program[p2i]
        return index + 4, relative_index

    def _3(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(p1i)
        program[p1i] = get(inputs)
        return index + 2, relative_index

    def _4(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(p1i)
        put(outputs, program[p1i])
        return index + 2, relative_index

    def _5(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(max(p1i, p2i))
        return program[p2i] if program[p1i] != 0 else index + 3, relative_index

    def _6(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(max(p1i, p2i))
        return program[p2i] if program[p1i] == 0 else index + 3, relative_index

    def _7(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(max(p1i, p2i, p3i))
        program[p3i] = int(program[p1i] < program[p2i])
        return index + 4, relative_index

    def _8(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(max(p1i, p2i, p3i))
        program[p3i] = int(program[p1i] == program[p2i])
        return index + 4, relative_index

    def _9(p1i, p2i, p3i, index, relative_index):
        extend_memory_if_necessary(p1i)
        return index + 2, relative_index + program[p1i]

    def _99(p1i, p2i, p3i, index, relative_index):
        return len(program), relative_index

    def mode(v, par_n):
        m = (v // 10 ** (par_n - 1)) % 10
        if m == 0:
            extend_memory_if_necessary(instr_ptr + par_n)
            return program[instr_ptr + par_n]
        elif m == 1:
            return instr_ptr + par_n
        elif m == 2:
            extend_memory_if_necessary(instr_ptr + par_n)
            return rel_ptr + program[instr_ptr + par_n]

    istr = {
        1: _1, 2: _2, 3: _3,
        4: _4, 5: _5, 6: _6,
        7: _7, 8: _8, 9: _9,
        99: _99,
    }

    while instr_ptr < len(program):
        op_code = program[instr_ptr] % 100
        par1_index = mode(program[instr_ptr] // 100, 1)
        par2_index = mode(program[instr_ptr] // 100, 2)
        par3_index = mode(program[instr_ptr] // 100, 3)
        if op_code != 3 or len(inputs) > 0:
            instr_ptr, rel_ptr = istr[op_code](par1_index, par2_index, par3_index, instr_ptr, rel_ptr)
        else:
            break  # blocking current execution until an input is provided
    return instr_ptr, rel_ptr  # to restore the execution later
