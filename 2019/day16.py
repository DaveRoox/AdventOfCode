from functools import reduce


def prod(inp, patt, phase):
    return abs(reduce(lambda acc, i: acc + inp[i] * patt[((i + 1) // phase) % len(patt)], range(len(inp)), 0)) % 10


def generate(digits, times):
    for _ in range(times):
        digits = list(map(lambda phase: prod(digits, [0, 1, 0, -1], phase + 1), range(len(digits))))
    return digits


with open('./day16.txt') as f:
    digits = list(map(int, list(f.readline())))
    print(*generate(digits[:], times=100)[:8], sep='')  # part 1
    offset = int(''.join(map(str, digits[:7])))
    digits *= 10000
    for _ in range(100):
        for i in range(len(digits) - 2, offset - 1, -1):
            digits[i] = (digits[i] + digits[i + 1]) % 10
    print(*digits[offset:offset + 8], sep='')  # part 2
