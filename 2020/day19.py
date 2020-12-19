from functools import reduce


def resolve(r, rules, sols):
    def cartesian_product_concat(v1, v2):
        return {s1 + s2 for s1 in v1 for s2 in v2}

    if r not in sols:
        if isinstance(rules[r], str):
            sols[r] = {rules[r]}
        else:
            matches = set()
            for subrule in rules[r]:
                matches = matches.union(
                    reduce(lambda acc, subr: cartesian_product_concat(acc, resolve(subr, rules, sols)), subrule, {''})
                )
            sols[r] = matches
    return sols[r]


def part1(rules, messages):
    print(len(set(messages).intersection(resolve('0', rules, {}))))


def part2(rules, messages):
    def is_in_0(m):
        if m in sols['0']:
            return True
        sub_m, upper = '', -1
        u = 0
        for i in range(len(m)):
            sub_m += m[i]
            if sub_m in sols['42']:
                sub_m, upper = '', i
                u += 1
        sub_m, lower = '', len(m)
        l = 0
        for j in range(len(m) - 1, upper, -1):
            sub_m = m[j] + sub_m
            if sub_m in sols['31']:
                sub_m, lower = '', j
                l += 1
        return u > l > 0 and upper == lower - 1

    sols = {}
    resolve('0', rules, sols)
    print(sum(map(is_in_0, messages)))


with open("input/day19.txt") as f:
    r, messages = list(map(lambda l: l.split('\n'), f.read().split('\n\n')))
    rules = {}
    for number, rule in (line.split(': ') for line in r):
        rules[number] = rule[1:-1] if 'a' <= rule[1:-1] <= 'z' else [r.split() for r in rule.split('|')]
    part1(rules, messages)
    part2(rules, messages)
