from functools import reduce


def part1(buses, timestamp):
    m, res = timestamp, None
    for bus in buses:
        if bus != 'x':
            bus = int(bus)
            tm = bus - timestamp % bus
            if tm < m:
                m, res = tm, tm * bus
    print(res)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    return gcd, y1 - (b // a) * x1, x1


def part2(buses):
    s, n = 0, reduce(lambda acc, b: acc * (int(b) if b != 'x' else 1), buses, 1)
    for i, b in enumerate(buses):
        if b != 'x':
            b = int(b)
            _, _, v = extended_gcd(b, n // b)
            e = v * n // b
            s -= i * e  # see the chinese remainder theorem for more info
    print(s % n)


with open("input/day13.txt") as f:
    t, v = int(f.readline()), f.readline().split(',')
    part1(v, t)
    part2(v)
