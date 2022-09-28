# 연습문제2

import sys
sys.stdin = open('input.txt')


def bfs(v):
    queue = []
    visited[v] = 1
    queue.append(v)
    route.append(v)

    while queue:
        t = queue.pop(0)
        for next_t in adj_list[t]:
            if not visited[next_t]:
                visited[next_t] = 1
                route.append(next_t)
                queue.append(next_t)


edge = list(map(int, input().split()))
adj_list = [[] for _ in range(8)]
N = len(edge) // 2

for i in range(N):
    v1, v2 = edge[i * 2], edge[i * 2 + 1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

visited = [0] * 8
route = []
bfs(1)
print(*route)
