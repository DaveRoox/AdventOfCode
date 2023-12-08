from functools import reduce
import math

def find_steps(path, nodes, start, end_pred):
    steps, curr, i = 0, start, 0
    while not end_pred(curr):
        direction = path[i]
        curr = nodes[curr][direction == 'R']
        steps += 1
        i = (i+1) % len(path)
    return steps


def part1(path, nodes):
    print(find_steps(path, nodes, start='AAA', end_pred=lambda n: n == 'ZZZ'))


def part2(path, nodes):
    print(reduce(math.lcm, (find_steps(path, nodes, start=n, end_pred=lambda nn: nn[-1] == 'Z') for n in nodes if n[-1] == 'A')))


with open("input/day08.txt") as f:
    path, nodes = f.read().split('\n\n')
    nodes = dict(map(lambda n: tuple(n.split(' = ')), nodes.split('\n')))
    nodes = {n:v[1:-1].split(', ') for n, v in nodes.items()}
    part1(path, nodes)
    part2(path, nodes)
