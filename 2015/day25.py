def f(i, j, sol):
    if i not in sol:
        sol[i] = {}
    if j not in sol[i]:
        if i != 0:
            sol[i][j] = j + i + f(i - 1, j, sol)
        elif j != 0:
            sol[i][j] = j + 1 + f(i, j - 1, sol)
        else:
            sol[i][j] = 1
    return sol[i][j]


def generate_code(n):
    code = 20151125
    while n > 1:
        code = (code * 252533) % 33554393
        n -= 1
    return code


row, col = 2981, 3075  # 1-based row e col target
row -= 1  # 0-based row
col -= 1  # 0-based col
solutions = {}
for c in range(col):  # computing bottom-up solutions
    f(0, c, solutions)
for r in range(row):
    f(r, col, solutions)
print(generate_code(n=f(row, col, solutions)))
