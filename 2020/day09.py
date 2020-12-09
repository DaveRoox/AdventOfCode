def find_n(numbers):
    s = set(numbers[:25])
    for i in range(25, len(numbers)):
        for j in range(i - 25, i):
            if numbers[i] - numbers[j] in s:
                break
        else:
            return numbers[i]
        s.remove(numbers[i - 25])
        s.add(numbers[i])


def part1(numbers):
    print(find_n(numbers))


def part2(numbers):
    n = find_n(numbers)
    low, high, s = 0, 1, numbers[0]
    while high < len(numbers):
        ns = s + numbers[high]
        if ns > n:
            s -= numbers[low]
            low += 1
        elif ns < n:
            s = ns
            high += 1
        else:
            v = numbers[low:high + 1]
            print(min(v) + max(v))
            return


with open("day09.txt") as f:
    nums = list(map(int, f.readlines()))
    part1(nums)
    part2(nums)
