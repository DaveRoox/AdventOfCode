from functools import reduce


def count_ingredient_occurrences(v):
    occs = {}
    for _, ingredients in v:
        for ingredient in ingredients:
            if ingredient not in occs:
                occs[ingredient] = 0
            occs[ingredient] += 1
    return occs


def possible_ingredients_by_allergen(v):
    ingrs_per_allergen = {}
    for allergens, ingredients in v:
        for allergen in allergens:
            if allergen not in ingrs_per_allergen:
                ingrs_per_allergen[allergen] = set(ingredients)
            else:
                ingrs_per_allergen[allergen] = ingrs_per_allergen[allergen].intersection(set(ingredients))
    return ingrs_per_allergen


def part1(v):
    occs = count_ingredient_occurrences(v)
    possible_ingrs_by_allergen = possible_ingredients_by_allergen(v)
    all_possible_ingredients_with_allergens = reduce(
        lambda acc, ingrs: acc.union(set(ingrs)),
        possible_ingrs_by_allergen.values(),
        set()
    )
    print(sum(occ for ingr, occ in occs.items() if ingr not in all_possible_ingredients_with_allergens))


def part2(v):
    def count_and_delete_repetitions():
        removed = 0
        for allergen, ingredients in ingrs_by_allergen.items():
            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                for another_allergen in ingrs_by_allergen:
                    if another_allergen != allergen and ingredient in ingrs_by_allergen[another_allergen]:
                        ingrs_by_allergen[another_allergen].remove(ingredient)
                        removed += 1
        return removed

    ingrs_by_allergen = possible_ingredients_by_allergen(v)
    while count_and_delete_repetitions() > 0:
        pass
    all_ingredients_with_allergens = reduce(
        lambda acc, ingrs: acc.union(set(ingrs)),
        ingrs_by_allergen.values(),
        set()
    )
    allergens_by_ingrs = {list(ingrs)[0]: a for a, ingrs in ingrs_by_allergen.items()}
    print(','.join(sorted(list(all_ingredients_with_allergens), key=lambda i: allergens_by_ingrs[i])))


with open("input/day21.txt") as f:
    v = []
    for line in f:
        ingredients, allergens = line.replace('\n', '')[:-1].split(' (contains ')
        v.append((allergens.split(', '), ingredients.split()))
    part1(v)
    part2(v)
