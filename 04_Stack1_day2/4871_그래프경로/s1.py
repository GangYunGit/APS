# 4871_그래프_경로

import sys
sys.stdin = open("input.txt")


def dfs(v):
    visited[v] = True

    for next_v in adj_list[v]:
        if not visited[next_v]:  # 방문하지 않았다면
            dfs(next_v)  # 인접 정점으로 이동

    return next_v


for test_case in range(1, int(input()) + 1):

    V, E = map(int, input().split())
    print(V, E)

    adj_list = [[] for _ in range(V + 1)]

    for _ in range(E):
        v_1, v_2 = map(int, input().split())
        adj_list[v_1].append(v_2)
    print(adj_list)

    S, G = map(int, input().split())
    print(S, G)

    visited = [False] * (V + 1)
    dfs(1)

    print()