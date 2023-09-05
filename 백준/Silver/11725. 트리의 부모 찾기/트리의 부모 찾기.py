from collections import deque


def bfs(v):
    visited = [False for _ in range(n + 1)]
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                parent_info[next_v] = v
                queue.append(next_v)


n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
graph = [[] for _ in range(n + 1)]
parent_info = [0] * (n + 1)

for v1, v2 in edges:
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(1)
print(*parent_info[2:], sep="\n")