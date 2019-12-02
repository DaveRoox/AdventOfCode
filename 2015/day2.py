from functools import reduce

with open('./day22015.txt') as f:
    wrapping_paper = 0
    feet_of_ribbon = 0
    for line in f:
        dims = list(map(int, (x for x in line.split('x'))))
        surf = [dims[0] * dims[1], dims[1] * dims[2], dims[2] * dims[0]]
        wrapping_paper += 2 * sum(surf) + min(surf)
        feet_of_ribbon += 2 * (sum(dims) - max(dims)) + reduce(lambda a, x: a * x, dims, 1)
    print(wrapping_paper)
    print(feet_of_ribbon)