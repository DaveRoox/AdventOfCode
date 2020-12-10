from math import ceil


def quantity_for(requested_qnt, mat, materials_map, bag):
    if mat == 'ORE' or requested_qnt == 0:
        return requested_qnt

    if mat in bag:
        if bag[mat] >= requested_qnt:
            bag[mat] -= requested_qnt
            return 0
        else:
            requested_qnt -= bag[mat]
            bag[mat] = 0

    recipe_qnt, needed_inputs = materials_map[mat]
    n_creations_required = ceil(requested_qnt / recipe_qnt)

    ore = 0
    for inp_qnt, inp_name in needed_inputs:
        ore += quantity_for(n_creations_required * inp_qnt, inp_name, materials_map, bag)

    bag[mat] = n_creations_required * recipe_qnt - requested_qnt

    return ore


def part1(materials_map):
    print(quantity_for(1, 'FUEL', materials_map, bag={}))


def part2(materials_map):
    pass


with open("input/day14.txt") as f:
    m = {}
    for inps, out in (line.replace('\n', '').split(' => ') for line in f):
        out_qnt, out_name = out.split(' ')
        m[out_name] = (int(out_qnt), [])
        for inp in inps.split(', '):
            i_q, i_n = inp.split(' ')
            m[out_name][1].append((int(i_q), i_n))
    part1(m)
    part2(m)
