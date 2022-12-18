# BOJ_1260. DFS와 BFS
from collections import deque


def dfs(v):
    visited_dfs[v] = True
    dfs_route.append(v)
    for next_v in graph[v]:
        if not visited_dfs[next_v]:
            dfs(next_v)


def bfs(v):
    visited_bfs[v] = True
    queue = deque()
    queue.append(v)
    bfs_route.append(v)

    while queue:
        temp_v = queue.popleft()
        for next_v in graph[temp_v]:
            if not visited_bfs[next_v]:
                visited_bfs[next_v] = True
                bfs_route.append(next_v)
                queue.append(next_v)


vertex, edge, start = map(int, input().split())
edge_list = [list(map(int, input().split())) for _ in range(edge)]

graph = [[] for _ in range(vertex + 1)]

for v1, v2 in edge_list:
    graph[v1].append(v2)
    graph[v2].append(v1)

for route in graph:
    route.sort()

visited_dfs = [False for _ in range(vertex + 1)]
visited_bfs = [False for _ in range(vertex + 1)]
dfs_route = []
bfs_route = []

dfs(start)
print(*dfs_route)
bfs(start)
print(*bfs_route)
