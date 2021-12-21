from aoc_utils import aoc_utils


def score(pos, n):
    return 1 + (pos + n - 1) % 10


@aoc_utils.memoized
def explore_solutions(p1_score_to_win, p2_score_to_win, p1_pos, p2_pos, p1_turn):
    if p1_score_to_win <= 0:
        return 1, 0
    if p2_score_to_win <= 0:
        return 0, 1
    p1_victories, p2_victories = 0, 0
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                pos = score(p1_pos if p1_turn else p2_pos, d1 + d2 + d3)
                p1v, p2v = explore_solutions(p1_score_to_win - (pos if p1_turn else 0),
                                             p2_score_to_win - (0 if p1_turn else pos),
                                             pos if p1_turn else p1_pos, p2_pos if p1_turn else pos, not p1_turn)
                p1_victories += p1v
                p2_victories += p2v
    return p1_victories, p2_victories


def part1(p1, p2):
    s1, s2, k = 0, 0, 0
    while s2 < 1000:
        p1 = score(p1, 3 * k + 6)
        s1 += p1
        k += 3
        if s1 >= 1000:
            break
        p2 = score(p2, 3 * k + 6)
        s2 += p2
        k += 3
    print(k * min(s1, s2))


def part2(p1, p2):
    print(max(explore_solutions(21, 21, p1, p2, True)))


with open("input/day21.txt") as f:
    p1, p2 = tuple(map(lambda l: int(l.replace('\n', '').split()[-1]), f.readlines()))
    part1(p1, p2)
    part2(p1, p2)
