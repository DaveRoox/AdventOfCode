def execute(program, inputs, outputs, istr_ptr=0, rel_i=0):
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
            extend_memory_if_necessary(istr_ptr + par_n)
            return program[istr_ptr + par_n]
        elif m == 1:
            return istr_ptr + par_n
        elif m == 2:
            extend_memory_if_necessary(istr_ptr + par_n)
            return rel_i + program[istr_ptr + par_n]

    istr = {
        1: _1, 2: _2, 3: _3,
        4: _4, 5: _5, 6: _6,
        7: _7, 8: _8, 9: _9,
        99: _99,
    }

    n = len(program) - 1
    while istr_ptr <= n:
        op_code = program[istr_ptr] % 100
        par1_index = mode(program[istr_ptr] // 100, 1)
        par2_index = mode(program[istr_ptr] // 100, 2)
        par3_index = mode(program[istr_ptr] // 100, 3)
        if op_code != 3 or len(inputs) > 0:
            istr_ptr, rel_i = istr[op_code](par1_index, par2_index, par3_index, istr_ptr, rel_i)
        else:
            break
    return istr_ptr, rel_i  # to restore the execution later


def update_dir_and_pos(dir, pos, turning_direction):
    dirs = {
        '<': [(+1, 0, 'v'), (-1, 0, '^')],
        '>': [(-1, 0, '^'), (+1, 0, 'v')],
        '^': [(0, -1, '<'), (0, +1, '>')],
        'v': [(0, +1, '>'), (0, -1, '<')],
    }
    dy, dx, dir = dirs[dir][turning_direction]  # turning left if 0, right if 1
    return dir, (pos[0] + dy, pos[1] + dx)


def get_painted_positions(program, default_color):
    positions = {}
    curr_dir, curr_pos = '^', (0, 0)
    index, rel_index, out = 0, 0, []
    while index < len(program):
        index, rel_index = execute(
            program, inputs=[positions.get(curr_pos, default_color)], outputs=out, istr_ptr=index, rel_i=rel_index)
        positions[curr_pos] = out.pop(0)  # painting the current position with the output color
        curr_dir, curr_pos = update_dir_and_pos(curr_dir, curr_pos, out.pop(0))
    return positions


def part1(program):
    print(len(get_painted_positions(program, default_color=0)))


def part2(program):
    positions = get_painted_positions(program, default_color=1)
    min_y, min_x = 0, 0
    max_y, max_x = 0, 0
    for pos in positions:
        min_y, min_x = min(min_y, pos[0]), min(min_x, pos[1])
        max_y, max_x = max(max_y, pos[0]), max(max_x, pos[1])
    print('\n'.join(
        ''.join(' *'[positions.get((y, x), 0)] for x in range(min_x, max_x + 1)) for y in range(min_y, max_y + 1)
    ))


with open("day11.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v)
