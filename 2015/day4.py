import hashlib


def md5_starts_with(prefix, key):
    n, l = 0, len(prefix)
    while True:
        if hashlib.md5((key + str(n)).encode('utf-8')).hexdigest()[:l] == prefix:
            return n
        n += 1


def part1(key):
    print(md5_starts_with('00000', key))


def part2(v):
    print(md5_starts_with('000000', key))


with open("input/day4.txt") as f:
    key = f.readline().replace('\n', '')
    part1(key)
    part2(key)
