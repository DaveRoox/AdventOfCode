from functools import reduce


def part1(expressions):
    def eval(expression, i=0):
        ops = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}
        res, n, op = 0, 0, '+'
        while i < len(expression) and expression[i] != ')':
            c = expression[i]
            if '0' <= c <= '9':
                n = 10 * n + int(c)
            elif c in ops:
                res = ops[op](res, n)
                n, op = 0, c
            elif c == '(':
                n, i = eval(expression, i + 1)
            i += 1
        return ops[op](res, n), i

    print(sum(eval(e)[0] for e in expressions))


def part2(expressions):
    def eval(expression, i=0):
        res, n, op = [0], 0, '+'
        while i < len(expression) and expression[i] != ')':
            c = expression[i]
            if '0' <= c <= '9':
                n = 10 * n + int(c)
            elif c in ('+', '*'):
                if op == '+':
                    res.append(res.pop() + n)
                else:
                    res.append(n)
                n, op = 0, c
            elif c == '(':
                n, i = eval(expression, i + 1)
            i += 1
        if op == '+':
            res.append(res.pop() + n)
            n = 1
        return reduce(lambda acc, operand: acc * operand, res, n), i

    print(sum(eval(e)[0] for e in expressions))


with open("input/day18.txt") as f:
    e = [line.replace('\n', '') for line in f]
    part1(e)
    part2(e)
