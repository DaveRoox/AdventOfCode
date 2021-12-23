from copy import deepcopy


def side_rooms():
    return [2, 4, 6, 8]


def hallway_rooms():
    return [0, 1, 3, 5, 7, 9, 10]


def has_no_obstacles(stacks, start, end):
    return all(idx in side_rooms() or len(stacks[idx]) == 0 for idx in range(start + 1, end))


def can_be_placed_in_dest_stack(stacks, n, el, curr_stack_index):
    dest_stack_index = 2 * (1 + ord(el) - ord('A'))
    # the item is already there
    if curr_stack_index == dest_stack_index:
        return False
    # the stack is full or contains items that don't belong there
    if len(stacks[dest_stack_index]) == n or any(x != el for x in stacks[dest_stack_index]):
        return False
    # there are no obstacles along the way from curr_stack_index to dest_stack_index
    return has_no_obstacles(stacks, min(curr_stack_index, dest_stack_index), max(curr_stack_index, dest_stack_index))


def minimum_energy(stacks, n, score=0):
    if stacks == [[], [], ['A'] * n, [], ['B'] * n, [], ['C'] * n, [], ['D'] * n, [], []]:
        return score

    # check if a movement for a final destination is available
    for i in range(len(stacks)):
        if len(stacks[i]) > 0 and can_be_placed_in_dest_stack(stacks, n, stacks[i][0], i):
            el = stacks[i][0]
            dest_stack_index = 2 * (1 + ord(el) - ord('A'))
            steps = abs(i - dest_stack_index)  # horizontal steps
            steps += n - len(stacks[dest_stack_index])  # down its stack
            if i in side_rooms():  # if curr stack is a side room
                steps += n + 1 - len(stacks[i])  # up curr stack
            stacks_cp = deepcopy(stacks)
            stacks_cp[dest_stack_index].append(el)
            stacks_cp[i].pop(0)
            return minimum_energy(stacks_cp, n, score + steps * {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[el])

    min_score = float('inf')
    for sr in side_rooms():
        if all(el == chr(sr // 2 - 1 + ord('A')) for el in stacks[sr]):
            continue  # side room empty or already full and complete
        stacks_cp = deepcopy(stacks)
        el = stacks_cp[sr].pop(0)
        for hr in hallway_rooms():
            # if this hallway room is empty and there are no obstascles along the way
            if len(stacks_cp[hr]) == 0 and has_no_obstacles(stacks_cp, min(sr, hr), max(sr, hr)):
                steps = abs(sr - hr)  # horizontal steps
                steps += n - len(stacks_cp[sr])  # up curr stack
                stacks_cp[hr] = [el]
                min_score = min(min_score,
                                minimum_energy(stacks_cp, n, score + steps * {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[
                                    el]))
                stacks_cp[hr] = []
    return min_score


def part1(stacks):
    print(minimum_energy(stacks, n=2))


def part2(stacks):
    stacks[2].insert(1, 'D')
    stacks[2].insert(1, 'D')
    stacks[4].insert(1, 'B')
    stacks[4].insert(1, 'C')
    stacks[6].insert(1, 'A')
    stacks[6].insert(1, 'B')
    stacks[8].insert(1, 'C')
    stacks[8].insert(1, 'A')
    print(minimum_energy(stacks, n=4))


with open("input/day23.txt") as f:
    lines = f.readlines()[2:4]
    v = [[lines[0][3 + 2 * k], lines[1][3 + 2 * k]] for k in range(4)]
    stacks = [[], [], v[0], [], v[1], [], v[2], [], v[3], [], []]
    part1(stacks)
    part2(stacks)
