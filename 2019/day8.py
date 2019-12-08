def find_digits(d, l):
    return sum(1 if c == d else 0 for c in l)


def decode_image(layers, H, W):
    image = []
    for h in range(H):
        for w in range(W):
            li = 0
            while li < len(layers) and layers[li][w + h * W] == '2':
                li += 1
            image.append('*' if layers[li][w + h * W] == '1' else ' ')
        image.append('\n')
    return image


with open('./day8.txt') as f:
    W, H = 25, 6
    pixels = f.readline()
    layer_size = W * H
    layers = [pixels[i * layer_size:(i + 1) * layer_size] for i in range(len(pixels) // layer_size)]
    layer = layers[min(map(lambda p: (p[0], find_digits('0', p[1])), enumerate(layers)), key=lambda p: p[1])[0]]
    print(find_digits('1', layer) * find_digits('2', layer))  # part 1
    print(''.join(decode_image(layers, H, W)))  # part 2
