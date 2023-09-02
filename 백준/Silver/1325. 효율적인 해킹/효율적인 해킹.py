from collections import deque
import sys


def bfs(v):
    visited = [False for _ in range(n + 1)]
    queue = deque()
    queue.append(v)
    visited[v] = True
    depth = 0

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                depth += 1

    hacked.append(depth)


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
hacked = [0]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v2].append(v1)

result = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    bfs(i)

max_hacked = max(hacked)
for i in range(1, n + 1):
    if hacked[i] == max_hacked:
        print(i, end=' ')