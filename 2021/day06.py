def children_per_fish(state, days, sols={}):
    if days <= state:
        return 0
    if (state, days) not in sols:
        sols[(state, days)] = 1 + (days-state-1)//7 + sum(children_per_fish(8, days-d) for d in range(state+1, days, 7))
    return sols[(state, days)]


def part1(fish_states):
    print(sum(1 + children_per_fish(state, days=80) for state in fish_states))


def part2(fish_states):
    print(sum(1 + children_per_fish(state, days=256) for state in fish_states))


with open("input/day06.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v)
    part2(v)
