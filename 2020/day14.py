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
    def addresses(a, m):
        for n in range(1 << m.count('X')):
            new_a = 0
            for i in range(len(m)):
                ii = len(m) - 1 - i
                bit = m[ii]
                if bit == '0':
                    new_a |= a & (1 << i)
                elif bit == '1':
                    new_a |= 1 << i
                else:
                    new_a |= (n & 1) << i
                    n >>= 1
            yield new_a

    mem = {}
    for mask, ops in total_ops:
        for addr, val in ops:
            for new_addr in addresses(addr, mask):
                mem[new_addr] = val
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
