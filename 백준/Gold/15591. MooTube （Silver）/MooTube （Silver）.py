import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def bfs(i):
    visited = [False for _ in range(N + 1)]
    visited[i] = True
    queue = deque()
    count = 0
    for v, weight in graph[i]:
        visited[v] = True
        queue.append((v, weight))

    while queue:
        v, weight = queue.popleft()
        if weight >= k:
            count += 1
            for next_v, next_weight in graph[v]:
                if not visited[next_v]:
                    visited[next_v] = True
                    queue.append((next_v, min(weight, next_weight)))

    return count


N, Q = map(int, input().split())
usado = [list(map(int, input().split())) for _ in range(N - 1)]
question = [list(map(int, input().split())) for _ in range(Q)]

graph = defaultdict(list)

for p, q, v in usado:
    graph[p].append((q, v))
    graph[q].append((p, v))

for k, v in question:
    print(bfs(v))