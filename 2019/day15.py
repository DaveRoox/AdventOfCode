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


def get_map(program):
    def visit(direction_code, pos):
        nonlocal istr_ptr, rel_i, codes_map
        inp.append(direction_code)
        istr_ptr, rel_i = execute(program, inp, out, istr_ptr, rel_i)
        codes_map[pos] = out.pop(0)
        return codes_map[pos]

    def opposite_direction(d):
        return 1 if d == 2 else 2 if d == 1 else 3 if d == 4 else 4

    def explore(curr_pos, dir_code):
        nonlocal oxygen_pos

        if curr_pos in codes_map:
            return False

        status_code = visit(dir_code, curr_pos)
        if status_code == 0:
            return False
        elif status_code == 2:
            oxygen_pos = curr_pos

        for k, new_pos in enumerate([
            (curr_pos[0], curr_pos[1] - 1),  # north
            (curr_pos[0], curr_pos[1] + 1),  # south
            (curr_pos[0] - 1, curr_pos[1]),  # west
            (curr_pos[0] + 1, curr_pos[1]),  # east
        ]):
            if explore(new_pos, k + 1):
                visit(opposite_direction(k + 1), curr_pos)  # stepping back
        return True

    istr_ptr, rel_i, inp, out = 0, 0, [], []  # Intcode computer-related variables
    codes_map, oxygen_pos = {}, None
    for k, v in enumerate([
        (0, -1),  # north
        (0, +1),  # south
        (-1, 0),  # west
        (+1, 0),  # east
    ]):
        if explore(v, k + 1):
            visit(opposite_direction(k + 1), (0, 0))

    return oxygen_pos, codes_map


def expand_from(src, codes_map, dest=None):
    q, res, visited = [(src, 0)], 0, set()
    while q:
        src, c = q.pop(0)
        if dest and src == dest:
            return c
        visited.add(src)
        for new_src in [
            (src[0], src[1] - 1),  # north
            (src[0], src[1] + 1),  # south
            (src[0] - 1, src[1]),  # west
            (src[0] + 1, src[1]),  # east
        ]:
            if new_src not in visited and new_src in codes_map and codes_map[new_src] != 0:
                q.append((new_src, c + 1))
        res = max(res, c)

    return res


def part1(program):
    print(expand_from(*get_map(program), dest=(0, 0)))


def part2(program):
    print(expand_from(*get_map(program)))


with open("day15.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v)
