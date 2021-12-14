from functools import reduce


def merge(d1, d2):
    d3 = {k: v for k, v in d1.items()}
    for k2 in d2:
        d3[k2] = d3.get(k2, 0) + d2[k2]
    return d3


def expand(pair, rules, n, cache):
    if n == 0:
        return {pair[0]: 1}
    if (pair, n) not in cache:
        cache[(pair, n)] = merge(expand(pair[0] + rules[pair], rules, n - 1, cache),
                                 expand(rules[pair] + pair[1], rules, n - 1, cache))
    return cache[(pair, n)]


def perform_steps(tmpl, rules, steps):
    cache = {}
    h = reduce(lambda h, pair: merge(h, expand(pair[0] + pair[1], rules, n=steps, cache=cache)),
               zip(tmpl, tmpl[1:]), {tmpl[-1]: 1})
    return max(h.values()) - min(h.values())


def part1(t, r):
    print(perform_steps(tmpl=t, rules=r, steps=10))


def part2(t, r):
    print(perform_steps(tmpl=t, rules=r, steps=40))


with open("input/day14.txt") as f:
    tmpl, rules = f.readline()[:-1], dict(map(lambda l: tuple(l.replace('\n', '').split(' -> ')), f.readlines()[1:]))
    part1(tmpl, rules)
    part2(tmpl, rules)
