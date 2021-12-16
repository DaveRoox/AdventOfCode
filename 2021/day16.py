from functools import reduce


def wrap_execution(bits):
    def extract_int(nbits):
        nonlocal idx
        idx += nbits
        return reduce(lambda acc, n: acc << 1 | n, bits[idx - nbits:idx])

    def extract_bit():
        return extract_int(nbits=1)

    def parse_number():
        number, can_continue = 0, True
        while can_continue:
            can_continue = extract_bit()
            number = number << 4 | extract_int(nbits=4)
        return number

    def parse_packet():
        nonlocal idx, version_numbers
        packet_version, type_id = extract_int(nbits=3), extract_int(nbits=3)
        version_numbers += packet_version

        if type_id == 4:
            return parse_number()
        else:
            numbers = []
            if extract_bit() == 0:
                total_length = extract_int(nbits=15)
                total_length += idx
                while idx < total_length:
                    numbers.append(parse_packet())
            else:
                numbers = [parse_packet() for _ in range(extract_int(nbits=11))]

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

    idx, version_numbers = 0, 0
    return parse_packet(), version_numbers


def part1(bits):
    print(wrap_execution(bits)[1])


def part2(bits):
    print(wrap_execution(bits)[0])


with open("input/day16.txt") as f:
    bits = reduce(lambda acc, x: acc + [(int(x, 16) & (1 << m)) >> m for m in range(3, -1, -1)],
                  f.readline().replace('\n', ''), [])
    part1(bits)
    part2(bits)
