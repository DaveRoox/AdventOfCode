def apply_phase(seats, n, occupied_adjacents):
    r = []
    for i in range(len(seats)):
        r.append('')
        for j in range(len(seats[0])):
            if seats[i][j] == '#':
                r[-1] += 'L' if occupied_adjacents(i, j) >= n else '#'
            elif seats[i][j] == 'L':
                r[-1] += '#' if occupied_adjacents(i, j) == 0 else 'L'
            else:
                r[-1] += '.'
    return r


def part1(seats):
    def occupied_adjacents(i, j):
        c = 0
        for di in [0, -1, +1]:
            if 0 <= i + di < len(seats):
                for dj in [0, -1, +1]:
                    if 0 <= j + dj < len(seats[0]):
                        if seats[i + di][j + dj] == '#':
                            c += 1
        return c - (seats[i][j] == '#')

    while True:
        new_seats = apply_phase(seats, 4, occupied_adjacents)
        if new_seats == seats:
            break
        seats = new_seats
    print(sum(map(lambda l: l.count('#'), seats)))


def part2(seats):
    def occupied_adjacents(i, j):
        c = 0
        for di in [0, -1, +1]:
            if 0 <= i + di < len(seats):
                for dj in [0, -1, +1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    while 0 <= ni < len(seats) and 0 <= nj < len(seats[0]):
                        if seats[ni][nj] != '.':
                            c += seats[ni][nj] == '#'
                            break
                        ni += di
                        nj += dj

        return c

    while True:
        new_seats = apply_phase(seats, 5, occupied_adjacents)
        if new_seats == seats:
            break
        seats = new_seats
    print(sum(map(lambda l: l.count('#'), seats)))


with open("input/day11.txt") as f:
    v = [line.replace('\n', '') for line in f]
    part1(v)
    part2(v)
