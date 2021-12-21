def index_for_position(input_image, i, j, background):
    n = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ni, nj = i + di, j + dj
            n <<= 1
            if ni < 0 or ni >= len(input_image) or nj < 0 or nj >= len(input_image[0]):
                n |= background
            elif input_image[ni][nj] == '#':
                n |= 1
    return n


def produce_output_image(iea, input_image, background):
    output_image_set = {(i, j) for i in range(-1, 1 + len(input_image)) for j in range(-1, 1 + len(input_image[0])) if
                        iea[index_for_position(input_image, i, j, background)] == '#'}
    return [['#' if (i, j) in output_image_set else '.' for j in range(-1, 1 + len(input_image[0]))]
            for i in range(-1, 1 + len(input_image))], {'.': 0, '#': 1}[iea[[0, -1][background]]]


def count_lit_after_n_steps(iea, input_image, n):
    background = 0
    for _ in range(n):
        input_image, background = produce_output_image(iea, input_image, background)
    return sum(line.count('#') for line in input_image)


def part1(iea, input_image):
    print(count_lit_after_n_steps(iea, input_image, n=2))


def part2(iea, input_image):
    print(count_lit_after_n_steps(iea, input_image, n=50))


with open("input/day20.txt") as f:
    iea, input_image = f.readline().replace('\n', ''), [l.replace('\n', '') for l in f.readlines()[1:]]
    part1(iea, input_image)
    part2(iea, input_image)
