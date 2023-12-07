def calibration_num(line):
    v = list(map(int, filter(lambda c: c.isdigit(), line)))
    return 10 * v[0] + v[-1]


def shrink(line):
    lookup_table = {n[:2]: (n, str(i+1)) for i, n in enumerate(
        ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])}
    new_line_parts, idx = [], 0
    while idx < len(line):
        new_line_part, offset, key = line[idx], 1, line[idx:idx+2]
        if key in lookup_table:
            target, replacement = lookup_table[key]
            if line[idx:idx+len(target)] == target:
                new_line_part, offset = replacement, len(target)
        new_line_parts.append(new_line_part)
        idx += offset
    return ''.join(new_line_parts)


def part1(lines):
    print(sum(map(calibration_num, lines)))


def part2(lines):
    print(sum(map(calibration_num, map(shrink, lines))))


with open("input/day01.txt") as f:
    lines = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    part1(lines)
    part2(lines)
