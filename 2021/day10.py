from functools import reduce
from statistics import median


def diagnose(v):
    stack, closing_map = [], {'{': '}', '(': ')', '<': '>', '[': ']'}
    for c in v:
        if c in closing_map:
            stack.append(c)
        elif not stack or c != closing_map[stack[-1]]:
            return True, c  # True if corrupted
        else:
            stack.pop()
    return False, ''.join(map(closing_map.get, stack[::-1]))  # False if incomplete


def part1(v):
    print(sum(map(lambda c: {')': 3, ']': 57, '}': 1197, '>': 25137}[c], v)))


def part2(v):
    print(median(map(lambda l: reduce(lambda score, c: 5 * score + {')': 1, ']': 2, '}': 3, '>': 4}[c], l, 0), v)))


with open("input/day10.txt") as f:
    corrupted, incomplete = [], []
    for l in map(diagnose, (line.replace('\n', '') for line in f.readlines())):
        is_corrupted, faulty = l
        if is_corrupted:
            corrupted.append(faulty)
        else:
            incomplete.append(faulty)
    part1(corrupted)
    part2(incomplete)
