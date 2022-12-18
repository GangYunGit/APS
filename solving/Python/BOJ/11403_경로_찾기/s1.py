# BOJ_11403. 경로 찾기

import sys
# sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(j):
    if len(route) > N:
        return

    route.append(j)
    for next_j in range(N):
        if graph[j][next_j] == 1:
            dfs(next_j)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            route = []
            dfs(j)
            for col in route:
                result[i][col] = 1

print(result)
