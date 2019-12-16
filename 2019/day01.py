def additional_fuel(x):
    if x <= 6:
        return 0
    x = x // 3 - 2
    return x + additional_fuel(x)


with open('day01.txt') as f:
    mass = [int(line) for line in f]
    print(sum(map(lambda m: m // 3 - 2, mass)))  # part 1
    print(sum(map(additional_fuel, mass)))  # part 2
