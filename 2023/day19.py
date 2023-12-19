class Predicate:
    def __init__(self, op, c=None, field=None):
        self.op = op
        self.c = c
        self.field = field

    def check(self, part):
        if self.op == '<':
            return part[self.field] < self.c
        if self.op == '>':
            return part[self.field] > self.c
        return True


def is_accepted(part, workflow, workflows):
    if workflow in ('A', 'R'):
        return workflow == 'A'
    for (pred, next_workflow) in workflows[workflow]:
        if pred.check(part):
            return is_accepted(part, next_workflow, workflows)
    return False


def find_all_accepted_constraints(workflow, workflows, constraints):
    if workflow == 'R':
        return []

    if workflow == 'A':
        return [constraints]

    all_subranges = []
    for (pred, next_workflow) in workflows[workflow]:
        new_constraints = {k: v for k, v in constraints.items()}
        if pred.op != '*':
            lo, hi = constraints[pred.field]
            nlo, nhi = constraints[pred.field]
            if pred.op == '<':
                hi = min(hi, pred.c - 1)
                nlo = pred.c
            if pred.op == '>':
                lo = max(lo, pred.c + 1)
                nhi = pred.c
            new_constraints[pred.field] = (lo, hi)
            constraints[pred.field] = (nlo, nhi)
        for sub_range in find_all_accepted_constraints(next_workflow, workflows, new_constraints):
            all_subranges.append(sub_range)
    return all_subranges


def combs(range):
    res = 1
    for k in range.keys():
        lo, hi = range[k]
        if lo > hi:
            return 0
        res *= hi - lo + 1
    return res


def intersection(range1, range2):
    range3 = {}
    for k in range1.keys():
        lo1, hi1 = range1[k]
        lo2, hi2 = range2[k]
        lo3, hi3 = max(lo1, lo2), min(hi1, hi2)
        range3[k] = (lo3, hi3)
    return range3


def distinct_combs(ranges):
    res = sum(combs(r) for r in ranges)
    for r1 in range(len(ranges) - 1):
        for r2 in range(r1 + 1, len(ranges)):
            res -= combs(intersection(ranges[r1], ranges[r2]))
    return res


def parse_desc(raw_desc):
    parts = raw_desc.split(':')
    for op in '<>=':
        cond_parts = parts[0].split(op)
        if len(cond_parts) > 1:
            return Predicate(op=op, c=int(cond_parts[1]), field=cond_parts[0]), parts[1]
    return Predicate(op='*'), parts[0]


def parse_workflow(raw_workflow):
    name, desc = raw_workflow.strip().split('{')
    return name, list(map(parse_desc, desc.split('}')[0].split(',')))


def parse_part(raw_part):
    return dict(map(lambda t: (t[0], int(t[1])), map(lambda v: tuple(v.split('=')), raw_part.strip()[1:-1].split(','))))


def part1(parts, workflows):
    print(sum(sum(part.values()) for part in parts if is_accepted(part, 'in', workflows)))


def part2(workflows):
    ranges = find_all_accepted_constraints('in', workflows, {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})
    print(distinct_combs(ranges))


with open("input/day19.txt") as f:
    raw_workflows, raw_parts = f.read().split('\n\n')
    workflows = dict(map(parse_workflow, raw_workflows.split('\n')))
    parts = list(map(parse_part, raw_parts.split('\n')))
    part1(parts, workflows)
    part2(workflows)
