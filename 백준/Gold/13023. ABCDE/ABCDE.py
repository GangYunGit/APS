import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(v, depth):
    global is_relation
    visited[v] = True

    if depth >= 4:
        is_relation = True
        return 

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, depth + 1)
            visited[next_v] = False


vertex, edge = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(edge)]
result = 0

graph = [[] for _ in range(vertex)]
for v1, v2 in relations:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False for _ in range(vertex)]

is_relation = False
for v in range(vertex):
    dfs(v, 0)

    if is_relation:
        result = 1
        break

    visited[v] = False

print(result)