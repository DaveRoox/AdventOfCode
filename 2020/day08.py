def part1(program):
    def execute(i, v, seen):
        if i >= len(program) or i in seen:
            return v
        seen.add(i)
        istr, op = program[i]
        return execute(i + 1, v + int(op), seen) if istr == 'acc' \
            else execute(i + int(op), v, seen) if istr == 'jmp' \
            else execute(i + 1, v, seen)

    print(execute(0, 0, set()))


def part2(program):
    def execute(i, v, seen, has_swapped):

        def try_(this, otherwise):
            try:
                return execute(this, v, seen, has_swapped)
            except RuntimeError as e:
                if not has_swapped:
                    return execute(otherwise, v, seen, True)
                else:
                    raise e

        if i in seen:
            raise RuntimeError('loop detected')
        if i >= len(program):
            return v
        seen.add(i)
        istr, op = program[i]
        return execute(i + 1, v + int(op), seen, has_swapped) if istr == 'acc' \
            else try_(this=i + int(op), otherwise=i + 1) if istr == 'jmp' \
            else try_(this=i + 1, otherwise=i + int(op))

    print(execute(0, 0, set(), False))


with open("day08.txt") as f:
    m = [line.replace('\n', '').split() for line in f]
    part1(m)
    part2(m)
