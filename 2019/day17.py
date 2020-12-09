import intcode


def find_path(grid, starting_position):
    def next_position():
        di, dj = {
            '^': (-1, 0),
            'v': (+1, 0),
            '<': (0, -1),
            '>': (0, +1),
        }[direction]
        return i + di, j + dj

    def next_direction():
        if direction in ('<', '>'):
            if i > 0 and grid[i - 1][j] == '#':
                return '^', {'<': 'R', '>': 'L'}[direction]
            elif i < len(grid) - 1 and grid[i + 1][j] == '#':
                return 'v', {'<': 'L', '>': 'R'}[direction]
        elif direction in ('^', 'v'):
            if j > 0 and grid[i][j - 1] == '#':
                return '<', {'^': 'L', 'v': 'R'}[direction]
            elif j < len(grid[0]) - 1 and grid[i][j + 1] == '#':
                return '>', {'^': 'R', 'v': 'L'}[direction]
        return None, ''

    i, j = starting_position
    direction = grid[i][j]
    path, count = [], 0

    while direction is not None:
        ni, nj = next_position()
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '#':  # keeps going
            i, j = ni, nj
            count += 1
        else:  # changes direction
            if count > 0:
                path.append(str(count))
                count = 0
            direction, cmd = next_direction()
            path.append(cmd)

    return path[:-1]


# Takes an input string in the form "R1L10R6R7" to produce a list in the form ["R", "1", "L", "10", "R", "6", "R", "7"]
def separate(s):
    res, t = [], ''
    for c in s:
        if '0' <= c <= '9':
            t += c
        else:
            if t:
                res.append(t)
                t = ''
            res.append(c)
    if t:
        res.append(t)
    return res


def split(l, cmds, n):
    if n == 0:
        return len(l) == l.count('-')
    low = 0
    while low < len(l) and l[low] == '-':
        low += 1
    if low == len(l):
        low = 0
    high = low
    while high < len(l) and l[high] != '-':
        high += 1
    for k in range(low, high):
        s = l[low:k + 1]
        t = l.replace(s, '-')
        if split(t, cmds, n - 1):
            cmds.append(separate(s))
            return True
    return False


def find_pattern(cmd_list, cmds):
    p, t = [], ''
    for cmd in cmd_list:
        t += cmd
        if t in cmds:
            p.append(cmds[t])
            t = ''
    if t in cmds:
        p.append(cmds[t])
    return p


def part1(program):
    out = []
    intcode.execute(program, inputs=[], outputs=out)
    last_row, curr_row, top, res = '', '', 0, 0
    while out:
        char = chr(out.pop(0))
        if char == '\n':
            if top > 0:
                for i in range(1, len(curr_row) - 1):
                    if [curr_row[i], curr_row[i - 1], curr_row[i + 1], last_row[i]].count('#') == 4:
                        res += i * top
            last_row, curr_row = curr_row, ''
            top += 1
        else:
            curr_row += char
    print(res)


def part2(program, is_interactive):
    def starting_position(g):
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] in ('^', '<', '>', 'v'):
                    return i, j

    # calculating the list of commands
    out = []
    intcode.execute(program[:], inputs=[], outputs=out)
    grid = list(filter(len, ''.join(map(chr, out)).split('\n')))
    cmd_list = find_path(grid, starting_position(grid))

    # splitting up the list of commands to find the command pattern
    cmds = []
    split(''.join(cmd_list), cmds, n=3)
    cmd_c, cmd_b, cmd_a = cmds
    cmd_m = find_pattern(cmd_list, cmds={''.join(cmd_a): 'A', ''.join(cmd_b): 'B', ''.join(cmd_c): 'C'})

    # initialising program params
    program[0] = 2
    out = []

    if is_interactive:
        print('The commands to provide are {}'.format(','.join(cmd_list)))
        print('Main is {}'.format(','.join(cmd_m)))
        print('Function A is {}'.format(','.join(cmd_a)))
        print('Function B is {}'.format(','.join(cmd_b)))
        print('Function C is {}'.format(','.join(cmd_c)))
        instr_ptr, rel_ptr, inp = 0, 0, []
        while True:
            out = []
            instr_ptr, rel_ptr = intcode.execute(program, inputs=inp, outputs=out, instr_ptr=instr_ptr, rel_ptr=rel_ptr)
            if instr_ptr < len(program):
                inp = list(map(ord, input(''.join(map(chr, out))))) + [10]
            else:
                break
    else:
        inp = [
            *list(map(ord, ','.join(cmd_m))), 10,
            *list(map(ord, ','.join(cmd_a))), 10,
            *list(map(ord, ','.join(cmd_b))), 10,
            *list(map(ord, ','.join(cmd_c))), 10,
            ord('n'), 10,
        ]
        intcode.execute(program, inputs=inp, outputs=out)

    print(out[-1])


with open("day17.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v, is_interactive=True)
