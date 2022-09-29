# 5249_최소신장트리

import sys
sys.stdin = open('input.txt')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


for test_case in range(1, int(input()) + 1):
    vertex, edge = map(int, input().split())
    edge_info = sorted([list(map(int, input().split())) for _ in range(edge)], key=lambda x: (x[2], x[0]))

    parent = [_ for _ in range(vertex + 1)]
    count = 0
    cost = 0

    for start, end, weight in edge_info:
        root_start, root_end = find_set(start), find_set(end)
        if root_start != root_end:
            parent[root_end] = root_start
            cost += weight
            count += 1

        if count == vertex:
            break
    print(parent)
    print(f'#{test_case} {cost}')
