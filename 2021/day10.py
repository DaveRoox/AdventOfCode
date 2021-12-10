from functools import reduce


def diagnose(line):
    stack, closing_map = [], {'{': '}', '(': ')', '<': '>', '[': ']'}
    for c in line:
        if c in closing_map:
            stack.append(c)
        elif len(stack) == 0 or c != closing_map[stack[-1]]:
            return True, c  # True if corrupted
        else:
            stack.pop()
    return False, ''.join(map(closing_map.get, stack[::-1]))  # False if incomplete


def part1(v):
    print(sum(map(lambda p: {')': 3, ']': 57, '}': 1197, '>': 25137}[p[1]] if p[0] else 0, map(diagnose, v))))


def part2(v):
    def get_score(l):
        return reduce(lambda score, c: 5 * score + {')': 1, ']': 2, '}': 3, '>': 4}[c], l, 0)

    scores = sorted(map(get_score, map(lambda p: p[1], filter(lambda p: not p[0], map(diagnose, v)))))
    print(scores[len(scores) // 2])


with open("input/day10.txt") as f:
    v = [line.replace('\n', '') for line in f.readlines()]
    part1(v)
    part2(v)
