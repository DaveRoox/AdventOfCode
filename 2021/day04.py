def is_bingo(num, line, unmarked):
    return num in line and len(unmarked.intersection(line)) == 0


def has_horizontal_bingo(board, num, unmarked):
    return any(is_bingo(num, row, unmarked) for row in board)


def has_vertical_bingo(board, num, unmarked):
    return any(
        is_bingo(num, col, unmarked) for col in ([board[i][j] for i in range(5)] for j in range(5)))


def has_bingo(board, num, unmarked):
    return has_horizontal_bingo(board, num, unmarked) or has_vertical_bingo(board, num, unmarked)


def part1(nums, boards):
    def check_for_bingo():
        unmarked_per_board = [{*board[0], *board[1], *board[2], *board[3], *board[4]} for board in boards]
        for num in nums:
            for board, unmarked in zip(boards, unmarked_per_board):
                if num in unmarked:
                    unmarked.remove(num)
                if has_bingo(board, num, unmarked):
                    return sum(unmarked) * num

    print(check_for_bingo())


def part2(nums, boards):
    def check_for_bingo():
        unmarked_per_board = [{*board[0], *board[1], *board[2], *board[3], *board[4]} for board in boards]
        last_bingo_score, bingo_done = None, set()
        for num in nums:
            for i, board in enumerate(boards):
                unmarked = unmarked_per_board[i]
                if num in unmarked:
                    unmarked.remove(num)
                if i not in bingo_done and has_bingo(board, num, unmarked):
                    last_bingo_score = sum(unmarked) * num
                    bingo_done.add(i)
        return last_bingo_score

    print(check_for_bingo())


with open("input/day04.txt") as f:
    v = list(f.readlines())
    nums = list(map(int, v[0].split(',')))
    boards = [list(map(lambda line: list(map(int, line.split())), (v[i + 1], v[i + 2], v[i + 3], v[i + 4], v[i + 5])))
              for i in range(1, len(v), 6)]
    part1(nums, boards)
    part2(nums, boards)
