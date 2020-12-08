import intcode


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
    instr_index, rel_index, out = 0, 0, []
    while instr_index < len(program):
        instr_index, rel_index = intcode.execute(
            program,
            inputs=[positions.get(curr_pos, default_color)],
            outputs=out,
            instr_ptr=instr_index,
            rel_ptr=rel_index
        )
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
