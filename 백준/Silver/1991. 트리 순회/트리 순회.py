def pre_order(node):
    print(tree[node][0], end='')
    for i in range(v):
        if tree[i][0] == tree[node][1]:
            pre_order(i)
    for i in range(v):
        if tree[i][0] == tree[node][2]:
            pre_order(i)


def in_order(node):
    for i in range(v):
        if tree[i][0] == tree[node][1]:
            in_order(i)
    print(tree[node][0], end='')
    for i in range(v):
        if tree[i][0] == tree[node][2]:
            in_order(i)


def post_order(node):
    for i in range(v):
        if tree[i][0] == tree[node][1]:
            post_order(i)
    for i in range(v):
        if tree[i][0] == tree[node][2]:
            post_order(i)
    print(tree[node][0], end='')


v = int(input())
tree = [input().split() for _ in range(v)]
pre_order(0)
print()
in_order(0)
print()
post_order(0)