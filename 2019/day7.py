import itertools
import queue
from threading import Thread


def run(program, queue_in, queue_out):
    p = 0
    while p < len(program):
        op_code = program[p] % 100
        if op_code == 99:  # exit
            return
        first_operand = program[program[p + 1]] if (program[p] % 1000) // 100 == 0 else program[p + 1]
        if op_code == 3:  # input
            program[program[p + 1]] = queue_in.get(block=True)
            p += 2
        elif op_code == 4:  # output
            queue_out.put(first_operand)
            p += 2
        else:
            second_operand = program[program[p + 2]] if (program[p] % 10000) // 1000 == 0 else program[p + 2]
            if op_code == 1:  # add
                program[program[p + 3]] = first_operand + second_operand
            elif op_code == 2:  # multiply
                program[program[p + 3]] = first_operand * second_operand
            elif op_code == 5:  # jump-if-true
                p = second_operand - 4 if first_operand != 0 else p - 1
            elif op_code == 6:  # jump-if-false
                p = second_operand - 4 if first_operand == 0 else p - 1
            elif op_code == 7:  # less-than
                program[program[p + 3]] = 1 if first_operand < second_operand else 0
            elif op_code == 8:  # equals
                program[program[p + 3]] = 1 if first_operand == second_operand else 0
            p += 4


def drive(program, permutation):  # starts 5 independent threads synchronized on a blocking queue
    n = len(permutation)
    queues = [queue.Queue() for _ in range(n)]
    for q, p in zip(queues, permutation):
        q.put(p)
    queues[0].put(0)
    amplifiers = []
    for a in range(n):
        amplifiers.append(Thread(target=run, args=(program[:], queues[a], queues[(a + 1) % 5])))
        amplifiers[-1].start()
    for t in amplifiers:  # waiting for them all to finish
        t.join()
    return queues[0].get()


with open('./day7.txt') as f:
    program = list(map(int, f.readline().split(',')))
    print(max(drive(program, permutation) for permutation in itertools.permutations(range(5))))  # part 1
    print(max(drive(program, permutation) for permutation in itertools.permutations(range(5, 10))))  # part 2
