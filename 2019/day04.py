def is_valid(n, func):
    last, n = n % 10, n // 10
    hist = [0 for _ in range(10)]
    hist[last] = 1
    while n > 0:
        curr = n % 10
        hist[curr] += 1
        if last < curr:
            return False
        last, n = curr, n // 10
    return any(map(func, hist))


def part1(rmin, rmax):
    print(sum(map(lambda n: is_valid(n, lambda v: v >= 2), range(max(rmin, 100000), min(rmax + 1, 999999)))))


def part2(rmin, rmax):
    print(sum(map(lambda n: is_valid(n, lambda v: v == 2), range(max(rmin, 100000), min(rmax + 1, 999999)))))


with open("day04.txt") as f:
    range_min, range_max = map(int, f.readline().split('-'))
    part1(range_min, range_max)
    part2(range_min, range_max)
