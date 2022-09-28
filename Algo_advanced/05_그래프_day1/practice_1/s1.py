# 연습문제1

import sys
sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = 1
    route.append(v)

    for next_v in adj_list[v]:
        if not visited[next_v]:
            visited[next_v] = 1
            dfs(next_v)


edge = list(map(int, input().split()))
adj_list = [[] for _ in range(8)]

for i in range(len(edge) // 2):
    v1, v2 = edge[i * 2], edge[i * 2 + 1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

visited = [0] * 8
route = []
dfs(1)
print(*route)
