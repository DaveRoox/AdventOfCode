def part1(modules):
    print(sum(map(lambda m: m // 3 - 2, modules)))


def part2(modules):
    def needed_fuel(module):
        s = 0
        while module > 0:
            module = max(module // 3 - 2, 0)
            s += module
        return s

    print(sum(map(needed_fuel, modules)))


with open("input/day01.txt") as f:
    v = list(map(int, f.readlines()))
    part1(v)
    part2(v)
