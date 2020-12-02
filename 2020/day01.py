def part1(nums):
    def find():
        s = set(nums)
        for x in s:
            if 2020 - x in s:
                return x * (2020 - x)
        return 0

    print(find())


def part2(nums):
    def find():
        s = set(nums)
        for x in s:
            for y in s:
                if 2020 - x - y in s:
                    return x * y * (2020 - x - y)
        return 0

    print(find())


with open("day01.txt") as f:
    v = list(map(int, f.readlines()))
    part1(v)
    part2(v)
