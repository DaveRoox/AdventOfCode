from itertools import permutations
import intcode


def part1(program):
    def evaluate_signal(phases):
        out = [0]
        for phase in phases:
            intcode.execute(program[:], inputs=[phase, out[-1]], outputs=out)
        return out[-1]

    print(max(map(evaluate_signal, permutations(range(5)))))


def part2(program):
    def evaluate_signal(phases):
        programs = [program[:] for _ in phases]
        instr_ptrs = [0 for _ in phases]
        inputs = [[phase] for phase in phases]
        inputs[0].append(0)

        i = 0
        while instr_ptrs[-1] < len(programs[-1]):
            next_i = (i + 1) % len(phases)
            instr_ptrs[i], _ = intcode.execute(programs[i], inputs[i], outputs=inputs[next_i], instr_ptr=instr_ptrs[i])
            i = next_i

        return inputs[0][-1]

    print(max(map(evaluate_signal, permutations(range(5, 10)))))


with open("day07.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v)
    part2(v)
