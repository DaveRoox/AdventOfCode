def location_for(seed, mappings):
    v = seed
    for mapping in mappings:
        for (dest, source, range) in mapping:
            if source <= v <= source + range:
                v = dest + v - source
                break
    return v


def seed_for(location, mappings):
    v = location
    for mapping in mappings[::-1]:
        for (dest, source, range) in mapping:
            if dest <= v <= dest + range:
                v = source + v - dest
                break
    return v


def part1(seeds, mappings):
    print(min(location_for(seed, mappings) for seed in seeds))


def part2(seeds, mappings):
    location, found = 0, False
    while not found:
        seed = seed_for(location, mappings)
        for (s, r) in zip(seeds[::2], seeds[1::2]):
            if s <= seed <= s + r:
                found = True
                break
        else:
            location += 1
    print(location)


with open("input/day05.txt") as f:
    blocks = f.read().split('\n\n')
    seeds = list(map(int, blocks[0].split(': ')[1].split()))
    mappings = [list(map(lambda m: tuple(map(int, m.split())),
                     block.split('\n')[1:])) for block in blocks[1:]]
    part1(seeds, mappings)
    part2(seeds, mappings)
