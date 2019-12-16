def num_descendants(node, children):
    if node not in children:  # `node` has no children
        return 0
    return len(children[node]) + sum(num_descendants(child, children) for child in children[node])


def path(node, root, parents):
    p = [node]
    while node != root:
        node = parents[node]
        p.append(node)
    return p


def lca_distance(node1, node2, root, parents):  # lowest common ancestor
    p1, p2 = path(node1, root, parents), path(node2, root, parents)
    i1, i2 = len(p1) - 1, len(p2) - 1
    while i1 >= 0 and i2 >= 0 and p1[i1] == p2[i2]:
        i1 -= 1
        i2 -= 1
    return i1 + i2


with open('day06.txt') as f:
    node_children, child_parent = {}, {}
    for line in f.readlines():
        p, c = line.replace('\n', '').split(')')
        if p not in node_children:  # `p` has no children yet
            node_children[p] = set()
        node_children[p].add(c)  # adding `child` as one of `parent`'s children
        child_parent[c] = p  # setting `parent` as `child`'s parent
    print(sum(num_descendants(parent, node_children) for parent in node_children.keys()))  # part 1
    print(lca_distance('YOU', 'SAN', 'COM', child_parent))  # part 2
