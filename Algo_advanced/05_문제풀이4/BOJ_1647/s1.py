# 1647_도시 분할 계획

import sys
sys.stdin = open('input.txt', encoding='utf-8')
input = sys.stdin.readline


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


vertex, edge = map(int, input().split())
edge_info = [list(map(int, input().split())) for _ in range(edge)]
edge_info.sort(key=lambda x: x[2])

parent = [_ for _ in range(vertex + 1)]
total_cost = 0
max_weight = 0

for start, end, weight in edge_info:
    root_1, root_2 = find_set(start), find_set(end)

    if root_1 != root_2:
        if weight > max_weight:
            max_weight = weight
        total_cost += weight
        parent[root_2] = root_1

result = total_cost - max_weight
print(result)
