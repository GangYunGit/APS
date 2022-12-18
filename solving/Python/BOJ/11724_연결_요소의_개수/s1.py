# BOJ_11724. 연결 요소의 개수

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    route.append(v)
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

    route.sort()
    return route


vertex, edge = map(int, input().split())
edge_list = [list(map(int, input().split())) for _ in range(edge)]
graph = [[] for _ in range(vertex + 1)]

for v1, v2 in edge_list:
    graph[v1].append(v2)
    graph[v2].append(v1)

connected = []
count = 0

for i in range(1, vertex + 1):
    if i in connected:
        continue
    visited = [False for _ in range(vertex + 1)]
    route = []
    dfs(i)
    count += 1
    connected += route

print(count)