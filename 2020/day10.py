def part1(numbers):
    numbers.sort()
    diffs = {numbers[0]: 1}
    for i in range(1, len(numbers)):
        d = numbers[i] - numbers[i - 1]
        if d not in diffs:
            diffs[d] = 0
        diffs[d] += 1
    print((1 + diffs[3]) * diffs[1])


def part2(numbers):
    numbers = [0] + sorted(numbers)
    sol = [0] * len(numbers)
    sol[-1] = 1
    for i in range(len(sol) - 2, -1, -1):
        j = i + 1
        while j < len(sol) and numbers[j] - numbers[i] <= 3:
            sol[i] += sol[j]
            j += 1
    print(sol[0])


with open("day10.txt") as f:
    v = list(map(int, f.readlines()))
    part1(v[:])
    part2(v)
