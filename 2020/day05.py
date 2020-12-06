def seat_id(boarding_pass):
    def search(sequence, upper):
        low, high = 0, (1 << len(sequence)) - 1
        for bit in sequence:
            mid = (low + high) // 2
            if bit == upper:
                low = mid + 1
            else:
                high = mid
        return low

    return 8 * search(boarding_pass[:7], upper='B') + search(boarding_pass[7:], upper='R')


def part1(boarding_passes):
    print(max(map(seat_id, boarding_passes)))


def part2(boarding_passes):
    found_sids = set(map(seat_id, boarding_passes))
    print(*list(filter(lambda sid: sid not in found_sids, range(min(found_sids), max(found_sids)))))


with open("day05.txt") as f:
    b = [line.replace('\n', '') for line in f]
    part1(b)
    part2(b)
