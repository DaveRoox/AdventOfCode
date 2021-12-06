def shift(states, days):
    for _ in range(days):
        states[0:8], states[8] = states[1:], states[0]
        states[6] += states[8]
    return sum(states)


def part1(states):
    print(shift(states, days=80))


def part2(states):
    print(shift(states, days=256))


with open("input/day06.txt") as f:
    states = [0] * 9
    for state in list(map(int, f.readline().split(','))):
        states[state] += 1
    part1(states[:])
    part2(states)
