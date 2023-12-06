from functools import reduce
from math import ceil, floor

def count_solutions(T, D):
    low = (T - (T*T - 4*D)**.5) / 2
    low = (low+1) if low.is_integer() else ceil(low)
    high = (T + (T*T - 4*D)**.5) / 2
    high = (high-1) if high.is_integer() else floor(high)
    return int(high - low + 1)

def part1(times_distances_pairs):
    print(reduce(int.__mul__, map(lambda item: count_solutions(*item), times_distances_pairs)))


def part2(times_distances_pairs):
    time = int(''.join(map(lambda p: str(p[0]), times_distances_pairs)))
    distance = int(''.join(map(lambda p: str(p[1]), times_distances_pairs)))
    print(count_solutions(time, distance))


with open("input/day06.txt") as f:
    times_distances_pairs = [(t, d) for t, d in zip(*list(map(lambda l: list(map(int, l.replace('\n', '').split(': ')[1].strip().split())), f.readlines())))]
    part1(times_distances_pairs)
    part2(times_distances_pairs)