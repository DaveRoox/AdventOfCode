from functools import reduce


def is_in_range(n, r):
    return r[0][0] <= n <= r[0][1] or r[1][0] <= n <= r[1][1]


def is_in_at_least_one_range(n, ranges):
    return any(map(lambda r: is_in_range(n, r), ranges))


def part1(rules, tickets):
    print(sum(num for ticket in tickets[1:] for num in ticket if not is_in_at_least_one_range(num, rules.values())))


def part2(rules, tickets):
    def is_valid_ticket(t):
        return all(map(lambda n: is_in_at_least_one_range(n, rules.values()), t))

    def find_all_compatible_ranges(n):
        return [i for i, r in enumerate(rules.values()) if is_in_range(n, r)]

    def intersected_ranges(column):
        return column, reduce(
            lambda s, row: s.intersection(set(candidates[row][column])),
            range(1, len(candidates)),
            set(candidates[0][column])
        )

    candidates = [[find_all_compatible_ranges(num) for num in ticket] for ticket in filter(is_valid_ticket, tickets)]
    intersections = [intersected_ranges(i) for i in range(len(candidates[0]))]  # intersections column by column
    intersections.sort(key=lambda p: len(p[1]))  # sorting based on the number of available intersections
    mapping = {}
    while intersections:
        col, s = intersections.pop(0)
        field_index = list(s)[0]
        mapping[field_index] = col
        for _, ts in intersections:
            if field_index in ts:
                ts.remove(field_index)
    print(reduce(lambda acc, p: acc * (tickets[0][mapping[p[0]]] if 'departure' in p[1] else 1), enumerate(rules), 1))


with open("input/day16.txt") as f:
    rules, my_ticket, tickets = list(map(lambda l: l.split('\n'), f.read().split('\n\n')))
    tickets = list(map(lambda l: list(map(int, l.split(','))), my_ticket[1:] + tickets[1:]))
    rules_dict = {}
    for field, ranges in (l.split(': ') for l in rules):
        rules_dict[field] = list(map(lambda r: tuple(map(int, r.split('-'))), ranges.split(' or ')))
    part1(rules_dict, tickets)
    part2(rules_dict, tickets)
