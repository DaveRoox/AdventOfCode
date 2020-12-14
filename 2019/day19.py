import intcode


def apply(program, i, j, out):
    intcode.execute(program[:], inputs=[j, i], outputs=out)
    return out.pop(0)


def part1(program):
    out = []
    print(sum(apply(program, i, j, out) for j in range(50) for i in range(50)))


def part2(program):
    def a(i, j):
        out = []
        return apply(program, i, j, out)

    # a(i, j) == 1 && a(i, j - 100) == 1 && a(i, j - 101) == 0 && a(i - 100, j) == 1 && a(i - 101, j) == 0
    for i in range(150, 10000):
        for j in range(101, 10000):
            if a(i, j) == 1 and a(i, j - 100) == 1 and a(i, j - 101) == 0 and a(i - 100, j) == 1 and a(i - 101, j) == 0:
                print(10000 * (j - 100) + i - 100)
                return


with open("input/day19.txt") as f:
    v = list(map(int, f.readline().split(',')))
    #part1(v[:])
    part2(v)
