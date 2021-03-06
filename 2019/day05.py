import intcode


def part1(program):
    out = []
    intcode.execute(program, inputs=[1], outputs=out)
    print(out[-1])


def part2(program):
    out = []
    intcode.execute(program, inputs=[5], outputs=out)
    print(out[-1])


with open("input/day05.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v[:])
    part2(v)
