class State:

    # constants
    dir_left = {'^': '<', '<': 'v', 'v': '>', '>': '^'}
    dir_right = {v: k for (k, v) in dir_left.items()}
    dirs = {'^': (-1, 0), '<': (0, -1), 'v': (+1, 0), '>': (0, +1)}

    def __init__(self, initial_color):
        self.pos = (0, 0)
        self.position_colors = {self.pos: initial_color}
        self.visited_positions = [self.pos]
        self.first_output = True
        self.dir = '^'
        self.minr, self.maxr = 0, 0
        self.minc, self.maxc = 0, 0

    def color(self):
        return self.position_colors[self.pos]

    def set_color(self, color):
        self.position_colors[self.pos] = color

    def visit(self, new_pos):
        self.visited_positions.append(new_pos)
        if new_pos not in self.position_colors:
            self.position_colors[new_pos] = 0
        self.pos = new_pos
        self.minr, self.maxr = min(self.minr, new_pos[0]), max(self.maxr, new_pos[0])
        self.minc, self.maxc = min(self.minc, new_pos[1]), max(self.maxc, new_pos[1])

    def draw(self):
        grid = [[0 for _ in range(state.maxc - state.minc + 1)] for _ in range(state.maxr - state.minr + 1)]
        for (r, c) in state.visited_positions:
            grid[r - state.minr][c - state.minc] = state.position_colors[(r, c)]
        return '\n'.join(''.join(map(lambda e: '*' if e else ' ', row)) for row in grid)

    def change(self, out):
        if self.first_output:
            self.set_color(out)
        else:
            if out == 0:  # turn left 90 degrees
                self.dir = State.dir_left[self.dir]
            else:  # turn right 90 degrees
                self.dir = State.dir_right[self.dir]
            self.visit((self.pos[0] + State.dirs[self.dir][0], self.pos[1] + State.dirs[self.dir][1]))
        self.first_output = not self.first_output


def index(program, p, x, rel_base):  # same as day 9
    v = 10 ** (x + 2)
    mode = (program[p] % v) // (v / 10)
    index = program[p + x] if mode == 0 else (p + x) if mode == 1 else (program[p + x] + rel_base)
    while len(program) <= index:
        program.append(0)
    return index


def run(program, inputs, outputs):  # same as day 9, it only takes 2 additional input/output callable objs
    p, i, rel_base = 0, 0, 0
    while p < len(program):
        op_code = program[p] % 100
        if op_code == 99:  # exit
            return
        first_index = index(program, p, 1, rel_base)
        if op_code == 3:  # input
            program[first_index] = inputs()
            p += 2
        elif op_code == 4:  # output
            outputs(program[first_index])
            p += 2
        elif op_code == 9:  # change relative base
            rel_base += program[first_index]
            p += 2
        else:  # two-parameter opcodes
            second_index = index(program, p, 2, rel_base)
            if op_code == 5:  # jump-if-true
                p = program[second_index] if program[first_index] != 0 else p + 3
            elif op_code == 6:  # jump-if-false
                p = program[second_index] if program[first_index] == 0 else p + 3
            else:  # three-parameter opcodes
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


with open('./day11.txt') as f:
    original_program = list(map(int, f.readline().split(',')))
    state = State(initial_color=0)
    run(original_program[:], state.color, state.change)
    print(len(state.position_colors))  # part 1
    state = State(initial_color=1)
    run(original_program[:], state.color, state.change)
    print(state.draw())  # part 2
