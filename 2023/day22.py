def overlap(b1, b2):
    (x11, y11, _), (x12, y12, _) = b1
    min_x1, max_x1, min_y1, max_y1 = min(x11, x12), max(x11, x12), min(y11, y12), max(y11, y12)
    (x21, y21, _), (x22, y22, _) = b2
    min_x2, max_x2, min_y2, max_y2 = min(x21, x22), max(x21, x22), min(y21, y22), max(y21, y22)
    on_x = min_x2 <= max_x1 if min_x1 <= min_x2 else min_x1 <= max_x2
    on_y = min_y2 <= max_y1 if min_y1 <= min_y2 else min_y1 <= max_y2
    return on_x and on_y


def brick_supports(bricks):
    bricks = sorted(bricks, key=lambda b: max(b[0][2], b[1][2]))
    supports_by_brick = {}
    for b1 in bricks:
        min_b1_z = min(b1[0][2], b1[1][2])
        # Find all overlapping bricks below b1
        supports_by_brick[b1] = [b2 for b2 in bricks if max(b2[0][2], b2[1][2]) < min_b1_z and overlap(b1, b2)]
    # Compute the final z coordinate for each brick based on its supporting bricks' final z coordinate
    final_z = {}
    for brick in bricks:
        highest_z_below = max((final_z[supporting_brick] for supporting_brick in supports_by_brick[brick]), default=0)
        height = max(brick[0][2], brick[1][2]) - min(brick[0][2], brick[1][2]) + 1
        final_z[brick] = highest_z_below + height
    # Finally, for each brick discard all supporting bricks whose final z is lower than the maximum final z for any
    # of the supporting bricks
    for brick in supports_by_brick.keys():
        highest_z_below = max((final_z[supporting_brick] for supporting_brick in supports_by_brick[brick]), default=0)
        supports_by_brick[brick] = list(filter(lambda b: final_z[b] == highest_z_below, supports_by_brick[brick]))
    return supports_by_brick


def get_supports_mapping(bricks):
    # Each brick (key) being supported by the corresponding list of bricks (values)
    supports_by_bricks = brick_supports(bricks)
    # Each brick (key) supporting the corresponding list of bricks (values)
    bricks_by_support = {brick: [] for brick in bricks}
    for brick in supports_by_bricks:
        for supporting_brick in supports_by_bricks[brick]:
            bricks_by_support[supporting_brick].append(brick)
    return supports_by_bricks, bricks_by_support


def simulate_brick_fall(brick, bricks_by_support, fallen, supports_by_bricks):
    for supported_brick in bricks_by_support[brick]:
        if len({*supports_by_bricks[supported_brick]}.difference(fallen)) == 0:
            fallen.add(supported_brick)
            simulate_brick_fall(supported_brick, bricks_by_support, fallen, supports_by_bricks)


def part1(bricks):
    supports_by_bricks, bricks_by_support = get_supports_mapping(bricks)
    print(sum(
        all(len(supports_by_bricks[supported_brick]) > 1 for supported_brick in bricks_by_support[brick]) for brick in
        bricks_by_support))


def part2(bricks):
    supports_by_bricks, bricks_by_support = get_supports_mapping(bricks)
    count = 0
    for brick in bricks:
        fallen_bricks = {brick}
        simulate_brick_fall(brick, bricks_by_support, fallen_bricks, supports_by_bricks)
        count += len(fallen_bricks) - 1  # do not count the initial brick
    print(count)


with open("input/day22.txt") as f:
    bricks = list(
        map(lambda l: tuple(map(lambda coords: tuple(map(int, coords.split(','))), l.replace('\n', '').split('~'))),
            f.readlines()))
    part1(bricks)
    part2(bricks)
