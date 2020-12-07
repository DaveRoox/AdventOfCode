def part1(colors_map):
    def find_containers_for(col, s):
        if col not in reverse_color_map:
            return
        for c in reverse_color_map[col]:
            s.add(c)
            find_containers_for(c, s)

    reverse_color_map = {}
    for color in colors_map:
        for _, inner_color in colors_map[color]:
            if inner_color not in reverse_color_map:
                reverse_color_map[inner_color] = []
            reverse_color_map[inner_color].append(color)

    s = set()
    find_containers_for('shiny gold', s)
    print(len(s))


def part2(colors_map):
    def required_bags_for(color):
        if color not in colors_map:
            return 1  # itself
        return 1 + sum(q * required_bags_for(c) for q, c in colors_map[color])

    print(required_bags_for('shiny gold') - 1)


with open("day07.txt") as f:
    m = {}
    for outer, inners in (line.replace('.\n', '').split(' contain ') for line in f):
        if inners == 'no other bags':
            continue
        outer = ' '.join(outer.split()[:-1])
        if outer not in m:
            m[outer] = []
        for inner in inners.split(', '):
            v = inner.split()
            m[outer].append((int(v[0]), ' '.join(v[1:-1])))
    part1(m)
    part2(m)
