def is_valid_pwd(n, f):
    adj = [0 for _ in range(10)]
    last, n = n % 10, n // 10
    while n > 0:
        curr = n % 10
        if curr > last:
            return False
        if curr == last:
            adj[curr] += 1
        last, n = curr, n // 10
    return any(map(f, adj))


with open('day04.txt') as f:
    range_min, range_max = map(int, f.readline().split('-'))
    range_min = max(range_min, 100000)
    range_max = min(range_max, 999999)
    print(sum(map(lambda num: is_valid_pwd(num, lambda v: v > 0), range(range_min, range_max + 1))))  # part 1
    print(sum(map(lambda num: is_valid_pwd(num, lambda v: v == 1), range(range_min, range_max + 1))))  # part 2
