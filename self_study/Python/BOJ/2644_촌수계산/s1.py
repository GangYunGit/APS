# BOJ_2644. 촌수계산
from collections import deque


def bfs(v):
    global depth
    depth += 1
    visited[v] = True
    queue = deque()
    queue.append((v, depth))

    while queue:
        v, depth = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, depth + 1))
                if next_v == p2:
                    return
    else:
        depth = -1


n = int(input())    # 노드 개수
p1, p2 = map(int, input().split())      # 촌수를 계산할 두 사람
m = int(input())    # 부모 자식간의 관계 수 (간선의 개수)
relation = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]

for v1, v2 in relation:
    graph[v1].append(v2)
    graph[v2].append(v1)

depth = 0
visited = [False for _ in range(n + 1)]

bfs(p1)
print(depth)