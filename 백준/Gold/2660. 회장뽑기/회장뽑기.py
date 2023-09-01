from collections import deque


def bfs(v):
    global score
    visited = [False for _ in range(n + 1)]
    queue = deque()
    queue.append((v, 0))
    visited[v] = True

    while queue:
        v, depth = queue.popleft()
        score = max(depth, score)
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, depth + 1))


n = int(input())
graph = [[] for _ in range(n + 1)]
while True:
    v1, v2 = map(int, input().split())
    if v1 == -1:
        break
    graph[v1].append(v2)
    graph[v2].append(v1)

member = [0 for _ in range(n + 1)]
candidate_list = []
candidate_score, candidate_num = 0, 0
min_score = 50
for i in range(1, n + 1):
    score = 0
    bfs(i)
    member[i] = score
    min_score = min(score, min_score)

candidate_score = min_score
for i in range(1, n + 1):
    if member[i] == min_score:
        candidate_list.append(i)
        candidate_num += 1

print(candidate_score, candidate_num)
print(*candidate_list)