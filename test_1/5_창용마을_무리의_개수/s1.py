# 7465_창용마을_무리의_개수

import sys
sys.stdin = open("input.txt")


def dfs(v):
    visited[v] = True
    stack.append(v)
    stack.sort()
    for next_v in adj_list[v]:
        if not visited[next_v]:
            dfs(next_v)


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    count = 0
    relation = []
    new_stack = []
    v_info = [list(map(int, input().split())) for _ in range(M)]

    adj_list = [[] for _ in range(N + 1)]
    for v1, v2 in v_info:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        stack = []
        dfs(i)
        relation.append(stack)

    # 검색해서 찾아보니 2차원 리스트는 set을 이용해서 중복을 제거하려면 이런 방식을 써야함
    new_relation = set(map(tuple, relation))

    print(f'#{test_case} {len(new_relation)}')
