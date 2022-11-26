def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def union(node_1, node_2):
    root_1, root_2 = find_set(node_1), find_set(node_2)
    if root_1 != root_2:
        if root_1 < root_2:
            parent[root_2] = root_1
        else:
            parent[root_1] = root_2


N = int(input())
M = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
travel_plan = list(map(int, input().split()))

parent = [_ for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == 1:
            union(i + 1, j + 1)

for i in range(len(travel_plan) - 1):
    if find_set(travel_plan[i]) == find_set(travel_plan[i + 1]):
        result = 'YES'
    else:
        result = 'NO'
        break

print(result)
