from functools import reduce


def part1(expressions):
    def eval(expression, i=0):
        n, operands, operations = 0, [], []
        while i < len(expression) and expression[i] != ')':
            c = expression[i]
            if '0' <= c <= '9':
                n = 10 * n + int(c)
            elif c in ('+', '*'):
                operands.append(n)
                operations.append(c)
                n = 0
            elif c == '(':
                n, i = eval(expression, i + 1)
            i += 1
        operands.append(n)
        n = operands.pop(0)
        while operations:
            op = operations.pop(0)
            if op == '+':
                n += operands.pop(0)
            else:
                n *= operands.pop(0)
        return n, i

    print(sum(eval(e)[0] for e in expressions))


def part2(expressions):
    def eval(expression, i=0):
        n, operands, operations = 0, [], []
        while i < len(expression) and expression[i] != ')':
            c = expression[i]
            if '0' <= c <= '9':
                n = 10 * n + int(c)
            elif c in ('+', '*'):
                operands.append(n)
                if len(operations) > 0 and operations[-1] == '+':
                    operations.pop()
                    operands.append(operands.pop() + operands.pop())
                operations.append(c)
                n = 0
            elif c == '(':
                n, i = eval(expression, i + 1)
            i += 1
        operands.append(n)
        if len(operations) > 0 and operations[-1] == '+':
            operands.append(operands.pop() + operands.pop())
        return reduce(lambda acc, operand: acc * operand, operands, 1), i

    print(sum(eval(e)[0] for e in expressions))


with open("input/day18.txt") as f:
    e = [line.replace('\n', '') for line in f]
    part1(e)
    part2(e)
