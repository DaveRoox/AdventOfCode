def part1(nums):
    c = 0
    for x, y in zip(nums, nums[1:]):
        if y > x:
            c += 1
    print(c)


def part2(nums):
    c = 0
    for x, y in zip(nums, nums[3:]):
        if y > x:
            c += 1
    print(c)


with open("input/day01.txt") as f:
    v = list(map(int, f.readlines()))
    part1(v)
    part2(v)
