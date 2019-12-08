def generate_code(row, column):
    limit = max(row, column)
    r, code = 1, 20151125
    codes = []
    while r <= limit:
        new_code_row = [code]
        for c in range(r):
            code = (code * 252533) % 33554393
            new_code_row.append(code)
        r += 1
        codes.append(new_code_row)
        print('Riga 1:', codes)
    return codes[row - 1][column - 1]


#print(generate_code(row=2981, column=3075))
print(generate_code(row=2, column=3))
