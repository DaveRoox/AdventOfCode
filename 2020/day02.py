def part1(lines):
    def is_valid(line):
        range, letter, pwd = line.split()
        range_min, range_max = map(int, range.split('-'))
        return range_min <= pwd.count(letter[:-1]) <= range_max

    print(sum(map(is_valid, lines)))


def part2(lines):
    def is_valid(line):
        range, letter, pwd = line.split()
        range_min, range_max = map(int, range.split('-'))
        return len(pwd) >= range_max and (pwd[range_min - 1], pwd[range_max - 1]).count(letter[:-1]) == 1

    print(sum(map(is_valid, lines)))


with open("day02.txt") as f:
    v = [line.replace('\n', '') for line in f]
    part1(v)
    part2(v)
