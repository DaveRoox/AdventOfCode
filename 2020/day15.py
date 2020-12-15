def extract(nums, n):
    last, turns = nums[-1], {n: i + 1 for i, n in enumerate(nums[:-1])}
    for turn in range(len(nums), n):
        turns[last], last = turn, 0 if last not in turns else turn - turns[last]
    return last


def part1(nums):
    print(extract(nums, 2020))


def part2(nums):
    print(extract(nums, 30000000))


with open("input/day15.txt") as f:
    v = list(map(int, f.readline().split(',')))
    part1(v)
    part2(v)
