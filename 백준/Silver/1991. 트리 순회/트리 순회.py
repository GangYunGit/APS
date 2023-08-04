def pre_order(node):
    if node == '.':
        return
    print(node, end='')
    pre_order(tree[node][0])
    pre_order(tree[node][1])


def in_order(node):
    if node == '.':
        return
    in_order(tree[node][0])
    print(node, end='')
    in_order(tree[node][1])


def post_order(node):
    if node == '.':
        return
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end='')


n = int(input())
tree = dict()
for _ in range(n):
    parent, left_child, right_child = input().split()
    tree[parent] = (left_child, right_child)

pre_order('A')
print()
in_order('A')
print()
post_order('A')