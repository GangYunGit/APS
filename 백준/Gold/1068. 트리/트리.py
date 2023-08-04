def pre_order(node):
    global count

    if node == delete_idx:
        return

    if not tree[node]:
        count += 1
        return

    for i in range(len(tree[node])):
        pre_order(tree[node][i])


n = int(input())
parent_info = list(map(int, input().split()))
delete_idx = int(input())
tree = {i: [] for i in range(n)}

count = 0
root_idx = 0

for i in range(n):
    if parent_info[i] != -1:
        tree[parent_info[i]].append(i)
    else:
        root_idx = i

for i in range(n):
    for j in range(len(tree[i])):
        if delete_idx in tree[i]:
            tree[i].remove(delete_idx)

tree.pop(delete_idx)
pre_order(root_idx)
print(count)