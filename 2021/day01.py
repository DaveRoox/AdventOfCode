def part1(nums):
    print(sum(map(lambda t: int.__lt__(*t), zip(nums, nums[1:]))))


def part2(nums):
    print(sum(map(lambda t: int.__lt__(*t), zip(nums, nums[3:]))))


with open("input/day01.txt") as f:
    v = list(map(int, f.readlines()))
    part1(v)
    part2(v)
