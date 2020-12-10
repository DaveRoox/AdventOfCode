def part1(nums):
    def find():
        s = set()
        for num in nums:
            if 2020 - num in s:
                return num * (2020 - num)
            s.add(num)
        return 0

    print(find())


def part2(nums):
    def find():
        s = set(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if 2020 - nums[i] - nums[j] in s:
                    return nums[i] * nums[j] * (2020 - nums[i] - nums[j])
        return 0

    print(find())


with open("input/day01.txt") as f:
    v = list(map(int, f.readlines()))
    part1(v)
    part2(v)
