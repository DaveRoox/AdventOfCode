import intcode


def get_map(program):
    def visit(direction_code, pos):
        nonlocal istr_ptr, rel_i, codes_map
        inp.append(direction_code)
        istr_ptr, rel_i = intcode.execute(program, inp, out, istr_ptr, rel_i)
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


with open("input/day15.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v)
