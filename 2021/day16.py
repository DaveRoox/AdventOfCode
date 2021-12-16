from functools import reduce


def wrap_execution(bits, vn_f=None):

    def extract_int(bit_length):
        nonlocal bits, i
        i += bit_length
        return reduce(lambda acc, n: acc << 1 | n, bits[i - bit_length:i])

    def parse_number():
        nonlocal bits, i
        number, can_continue = 0, True
        while can_continue:
            can_continue = extract_int(bit_length=1)
            number = number << 4 | extract_int(bit_length=4)
        return number

    def parse_packet():
        nonlocal bits, i, vn_f
        packet_version, type_id = extract_int(bit_length=3), extract_int(bit_length=3)
        if vn_f:
            vn_f(packet_version)

        if type_id == 4:
            return parse_number()

        numbers, length_type_id = [], extract_int(bit_length=1)
        if length_type_id == 0:
            total_length = extract_int(bit_length=15)
            total_length += i
            while i < total_length:
                numbers.append(parse_packet())
        else:
            numbers = [parse_packet() for _ in range(extract_int(bit_length=11))]

        if type_id == 0:
            return sum(numbers)
        if type_id == 1:
            return reduce(int.__mul__, numbers, 1)
        if type_id == 2:
            return min(numbers)
        if type_id == 3:
            return max(numbers)
        if type_id == 5:
            return 1 if numbers[0] > numbers[1] else 0
        if type_id == 6:
            return 1 if numbers[0] < numbers[1] else 0
        return 1 if numbers[0] == numbers[1] else 0

    i = 0
    return parse_packet()


def part1(bits):
    def add_to_version_number(vn):
        nonlocal version_numbers
        version_numbers += vn

    version_numbers = 0
    wrap_execution(bits, vn_f=add_to_version_number)
    print(version_numbers)


def part2(bits):
    print(wrap_execution(bits))


with open("input/day16.txt") as f:
    bits = reduce(lambda acc, x: acc + [(int(x, 16) & (1 << m)) >> m for m in range(3, -1, -1)],
                  f.readline().replace('\n', ''), [])
    part1(bits)
    part2(bits)
