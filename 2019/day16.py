from functools import reduce


def part1(input_signal):
    def apply_phase(signal):
        out_signal, s = [], len(signal)
        for pos in range(1, s + 1):
            out_signal.append(abs(
                sum(sum(signal[i:i + pos]) for i in range(pos - 1, s, 4 * pos)) -
                sum(sum(signal[i:i + pos]) for i in range(pos - 1 + 2 * pos, s, 4 * pos))
            ) % 10)
        return out_signal

    print(*reduce(lambda s, _: apply_phase(s), range(100), input_signal)[:8], sep='')


def part2(signal):
    offset = int(''.join(map(str, signal[:7])))
    signal *= 10000
    for _ in range(100):
        for i in range(len(signal) - 2, offset - 1, -1):
            signal[i] = (signal[i] + signal[i + 1]) % 10

    print(*signal[offset:offset + 8], sep='')


with open("input/day16.txt") as f:
    m = list(map(int, f.readline()))
    part1(m)
    part2(m)
