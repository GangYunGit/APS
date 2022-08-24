# DFS_구현

import sys
sys.stdin = open('input.txt')


def bfs(v):
    visited[v] = True
    queue.append(v)
    print(v, end=' ')

    while queue:
        t = queue.pop(0)
        for next_t in adj_list[t]:
            if not visited[next_t]:
                visited[next_t] = True
                queue.append(next_t)
                print(next_t, end=' ')


vertex, edge = map(int, input().split())
edge_info = list(map(int, input().split()))

adj_list = [[] for _ in range(vertex + 1)]

for v in range(0, len(edge_info), 2):
    adj_list[edge_info[v]].append(edge_info[v + 1])
    adj_list[edge_info[v + 1]].append(edge_info[v])

visited = [False] * (vertex + 1)
queue = []
bfs(1)