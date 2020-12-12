def part1(moves):
    def step():
        nonlocal i, j, wp_j, wp_i, n
        if c == 'E':
            j += n
        elif c == 'W':
            j -= n
        elif c == 'N':
            i -= n
        elif c == 'S':
            i += n
        elif c == 'F':
            i += wp_i * n
            j += wp_j * n
        elif c == 'R':
            while n:
                wp_i, wp_j = wp_j, -wp_i
                n -= 90
        elif c == 'L':
            while n:
                wp_i, wp_j = -wp_j, wp_i
                n -= 90

    i, j, wp_i, wp_j = 0, 0, 0, 1
    for c, n in moves:
        step()
    print(abs(i) + abs(j))


def part2(moves):
    def step():
        nonlocal i, j, wp_j, wp_i, n
        if c == 'E':
            wp_j += n
        elif c == 'W':
            wp_j -= n
        elif c == 'N':
            wp_i -= n
        elif c == 'S':
            wp_i += n
        elif c == 'F':
            i += wp_i * n
            j += wp_j * n
        elif c == 'R':
            while n:
                wp_i, wp_j = wp_j, -wp_i
                n -= 90
        elif c == 'L':
            while n:
                wp_i, wp_j = -wp_j, wp_i
                n -= 90

    i, j, wp_i, wp_j = 0, 0, -1, 10
    for c, n in moves:
        step()
    print(abs(i) + abs(j))


with open("input/day12.txt") as f:
    v = [(line[0], int(line[1:])) for line in f]
    part1(v)
    part2(v)
