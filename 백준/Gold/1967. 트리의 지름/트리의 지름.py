import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def dfs(node, distance):
    global max_distance, leaf_node
    if max_distance < distance:
        max_distance = distance
        leaf_node = node

    for next_node, next_weight in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, distance + next_weight)
            visited[next_node] = False


n = int(input())
edge_info = [list(map(int, input().split())) for _ in range(n - 1)]
tree = [[] for _ in range(n + 1)]

for parent, child, weight in edge_info:
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

visited = [False] * (n + 1)
leaf_node = 0
max_distance = 0
visited[1] = True
dfs(1, 0)

visited = [False] * (n + 1)
max_distance = 0
visited[leaf_node] = True
dfs(leaf_node, 0)
print(max_distance)
