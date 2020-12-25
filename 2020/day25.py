from functools import reduce


def part1(card_pk, door_pk):
    v, loop_size = 1, 0
    while v != card_pk:
        v = (v * 7) % 20201227
        loop_size += 1
    print(reduce(lambda acc, _: (acc * door_pk) % 20201227, range(loop_size), 1))


def part2():
    print('Congratulations and merry Christmas!')


with open("input/day25.txt") as f:
    c_pk, d_pk = list((map(int, f.readlines())))
    part1(c_pk, d_pk)
    part2()
