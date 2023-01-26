from collections import deque


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
distances.sort(key=lambda x: (-x[1], x[0]))

hutgan_num, hutgan_distance, same_hutgan = distances[0][0], distances[0][1], 0
for n, d in distances:
    if d == hutgan_distance:
        same_hutgan += 1

print(hutgan_num, hutgan_distance, same_hutgan)