def part1(total_ops):
    def masks(m):
        and_m, or_m = (1 << 37) - 1, 0
        for i, bit in enumerate(m[::-1]):
            if bit == '0':
                and_m &= ~(1 << i)
            elif bit == '1':
                or_m |= 1 << i
        return and_m, or_m

    mem = {}
    for mask, ops in total_ops:
        and_mask, or_mask = masks(mask)
        for addr, val in ops:
            mem[addr] = val & and_mask | or_mask
    print(sum(mem.values()))


def part2(total_ops):
    def apply(n, p, positions):  # n is the number codified by the bits to replace the Xs in p with
        s = list(p)
        for i, pos in enumerate(positions):
            s[pos] = str((n & (1 << i)) >> i)
        return ''.join(s)

    def generate(p):
        positions = [i for i, c in enumerate(p) if c == 'X']
        return [apply(n, p, positions) for n in range(1 << len(positions))]

    def addresses(a, pattern):
        def ith_bit(i):
            return (a & (1 << i)) >> i

        addr = [str(ith_bit(i)) if c == '0' else c for i, c in enumerate(pattern[::-1])]
        return map(lambda a: int(a, 2), generate(addr))

    mem = {}
    for mask, ops in total_ops:
        for addr, val in ops:
            for a in addresses(addr, mask):
                mem[a] = val
    print(sum(mem.values()))


with open("input/day14.txt") as f:
    v = [line.replace('\n', '') for line in f]
    t_ops, mask, ops = [], None, []
    for line in v:
        if 'mask' in line:
            if mask:
                t_ops.append((mask, ops))
                ops = []
            mask = line.split(' = ')[1]
        else:
            mem, val = line.split(' = ')
            ops.append((int(mem[4:-1]), int(val)))
    if mask:
        t_ops.append((mask, ops))
    part1(t_ops)
    part2(t_ops)
