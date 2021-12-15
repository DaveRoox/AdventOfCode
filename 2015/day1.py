def part1(v):
    print(v.count('(') - v.count(')'))


def part2(v):
    floor = 0
    for i, c in enumerate(v):
        floor += [-1, 1][c == '(']
        if floor == -1:
            print(i+1)
            return


with open("input/day1.txt") as f:
    v = f.readline()
    part1(v)
    part2(v)
