def part1(line, width, height):
    layer_size = width * height
    layer = min(map(lambda i: line[i:i + layer_size], range(0, len(line), layer_size)), key=lambda lr: lr.count('0'))
    print(layer.count('1') * layer.count('2'))


def part2(line, width, height):
    def get_color(pixel_index):
        while pixel_index < len(line) and line[pixel_index] == '2':
            pixel_index += layer_size
        return line[pixel_index] if pixel_index < len(line) else '2'

    layer_size = width * height
    print('\n'.join(''.join(' *'[get_color(width * i + j) == '1'] for j in range(width)) for i in range(height)))


with open("day08.txt") as f:
    l = f.readline()
    part1(l, width=25, height=6)
    part2(l, width=25, height=6)
