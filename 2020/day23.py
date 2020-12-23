class node:
    def __init__(self, value):
        self.value = value
        self.next = None


def linked_list(values):
    head = node(values[0])
    curr = head
    for i in range(1, len(values)):
        curr.next = node(values[i])
        curr = curr.next
    curr.next = head
    return head


def play(head, iterations, minn, maxx):
    def get_dict():
        d = {head.value: head}
        curr = head.next
        while curr != head:
            d[curr.value] = curr
            curr = curr.next
        return d

    nodes_by_val = get_dict()
    current = head
    for _ in range(iterations):
        a = current.next
        b = a.next
        c = b.next
        current.next = c.next
        destination_cup = current.value - 1 if current.value != minn else maxx
        while destination_cup in (a.value, b.value, c.value):
            destination_cup -= 1
            if destination_cup < minn:
                destination_cup = maxx
        destination = nodes_by_val[destination_cup]
        c.next = destination.next
        destination.next = a
        current = current.next

    return nodes_by_val[1]


def part1(v):
    n = play(head=linked_list(v), iterations=100, minn=min(v), maxx=max(v))
    m, res = n.next, ''
    while m != n:
        res += str(m.value)
        m = m.next
    print(res)


def part2(v):
    minn = min(v)
    for k in range(max(v) + 1, 1_000_001):
        v.append(k)
    n = play(head=linked_list(v), iterations=10_000_000, minn=minn, maxx=1_000_000).next
    print(n.value * n.next.value)


with open("input/day23.txt") as f:
    v = list(map(int, f.read()))
    part1(v)
    part2(v)
