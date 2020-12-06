def positions(wire_movement):
    moves = {'R': (0, +1), 'L': (0, -1), 'U': (-1, 0), 'D': (+1, 0)}
    d, x, y, steps = {}, 0, 0, 0
    for movement in wire_movement:
        p = moves[movement[0]]
        for _ in range(int(movement[1:])):
            steps += 1
            y += p[0]
            x += p[1]
            if (x, y) not in d:
                d[(x, y)] = steps
    return d


def part1(wire1_moves, wire2_moves):
    steps1, steps2 = positions(wire1_moves), positions(wire2_moves)
    print(min(map(lambda p: abs(p[0]) + abs(p[1]), set(steps1.keys()).intersection(set(steps2.keys())))))


def part2(wire1_moves, wire2_moves):
    steps1, steps2 = positions(wire1_moves), positions(wire2_moves)
    print(min(map(lambda p: steps1[p] + steps2[p], set(steps1.keys()).intersection(set(steps2.keys())))))


with open("day03.txt") as f:
    w1, w2 = list(map(lambda l: l.split(','), (line.replace('\n', '') for line in f)))
    part1(w1, w2)
    part2(w1, w2)
