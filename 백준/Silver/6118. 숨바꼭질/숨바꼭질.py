from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    visited = [False for _ in range(N + 1)]
    visited[v] = True
    depth = 0
    queue = deque()
    queue.append((v, depth))

    while queue:
        v, depth = queue.popleft()
        distances.append((v, depth))
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, depth + 1))


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
distances = []

for v1, v2 in edges:
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(1)
max_distance = distances[-1][1]
result = []
for i in range(len(distances) - 1, -1, -1):
    if distances[i][1] == max_distance:
        result.append((distances[i][0], distances[i][1]))
    else:
        break
print(*min(result), len(result))
