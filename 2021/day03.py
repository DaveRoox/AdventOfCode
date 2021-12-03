from functools import reduce


def most_common_bit(nums, pos):
    return int(sum(num[pos] == '1' for num in nums) >= len(nums) / 2)


def least_common_bit(nums, pos):
    return 1 - most_common_bit(nums, pos)


def part1(nums):
    gamma_rate = reduce(lambda acc, pos: (acc << 1) | most_common_bit(nums, pos), range(len(nums[0])))
    print(gamma_rate * (~gamma_rate & ((1 << len(nums[0])) - 1)))


def part2(nums):
    def filter_down(arr, strategy):
        pos = 0
        while len(arr) > 1:
            res = str(strategy(arr, pos))
            arr = list(filter(lambda n: n[pos] == res, arr))
            pos += 1
        return int(arr[0], 2)

    print(filter_down(nums, most_common_bit) * filter_down(nums, least_common_bit))


with open("input/day03.txt") as f:
    v = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    part1(v)
    part2(v)
