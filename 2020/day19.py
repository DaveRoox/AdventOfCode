from functools import reduce


def resolve(r, rules, sols):
    def cartesian_product_concat(v1, v2):
        return {s1 + s2 for s1 in v1 for s2 in v2}

    if r not in sols:
        if isinstance(rules[r], str):
            sols[r] = [rules[r]]
        else:
            matches = set()
            for subrule in rules[r]:
                matches = matches.union(
                    reduce(lambda acc, subr: cartesian_product_concat(acc, resolve(subr, rules, sols)), subrule, [''])
                )
            sols[r] = matches
    return sols[r]


def part1(rules, messages):
    print(len(set(messages).intersection(resolve('0', rules, {}))))


def part2(rules, messages):
    def is_n(s, n):
        if n == '8':
            for i in range(len(s) + 1):
                if is_n(s[:i], '42') and (i == len(s) or is_n(s[i:], '8')):
                    return True
            return False
        elif n == '11':
            for i in range(len(s) + 1):
                for j in range(i, len(s) + 1):
                    if is_n(s[:i], '42') and (i == j or is_n(s[i:j], '11')) and is_n(s[j:], '31'):
                        return True
            return False
        return s in sols[n]

    sols = {}
    resolve('0', rules, sols)  # to populate sols
    print(sum(1
              for message in messages
              for i in range(1, len(message))
              if is_n(message[:i], '8') and is_n(message[i:], '11'))
          )


with open("input/day19.txt") as f:
    r, messages = list(map(lambda l: l.split('\n'), f.read().split('\n\n')))
    rules = {}
    for number, rule in (line.split(': ') for line in r):
        rules[number] = rule[1:-1] if 'a' <= rule[1:-1] <= 'z' else [r.split() for r in rule.split('|')]
    part1(rules, messages)
    part2(rules, messages)
