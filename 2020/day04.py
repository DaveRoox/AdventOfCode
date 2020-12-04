def part1(passports):
    def is_valid(passport):
        for b in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if b not in passport:
                return False
        return True

    print(sum(map(is_valid, passports)))


def part2(passports):
    def is_valid(passport):
        for b, cond in [
            ('byr', lambda v: 1920 <= int(v) <= 2002),
            ('iyr', lambda v: 2010 <= int(v) <= 2020),
            ('eyr', lambda v: 2020 <= int(v) <= 2030),
            ('hgt', lambda v: v[-2:] in ('cm', 'in') and
                              150 <= int(v[:-2]) <= 193 if v[-2:] == 'cm' else 59 <= int(v[:-2]) <= 76),
            ('hcl', lambda v: v[0] == '#' and all(map(lambda c: '0' <= c <= '9' or 'a' <= c <= 'f', v[1:]))),
            ('ecl', lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')),
            ('pid', lambda v: len(v) == 9 and all(map(lambda c: '0' <= c <= '9', v)))
        ]:
            if b not in passport or not cond(passport[b]):
                return False
        return True

    print(sum(map(is_valid, passports)))


def fold_multiline(v):
    nv, t = [], ''
    for p in v:
        if not p:
            if t:
                nv.append(t)
                t = ''
        else:
            if t:
                t += ' ' + p
            else:
                t = p
    if t:
        nv.append(t)
    return nv


with open("day04.txt") as f:
    v = list(map(lambda p: dict(map(lambda a: a.split(':'), p.split())), fold_multiline([line.replace('\n', '') for line in f])))
    part1(v)
    part2(v)
