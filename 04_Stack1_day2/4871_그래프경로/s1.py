# 4871_그래프_경로

import sys

sys.stdin = open("input.txt")


def dfs(v):
    visited[v] = True  # 방문했다는 표시
    stack.append(v)  # 방문한 지점을 스택에 쌓음

    for next_v in adj_list[v]:  # 인접한 모든 정점에 대하여
        if not visited[next_v]:  # 방문하지 않았다면
            dfs(next_v)  # 인접 정점으로 이동


for test_case in range(1, int(input()) + 1):
    result = 0

    # 정점(vertex), 간선(edge) 입력
    V, E = map(int, input().split())

    # 인접 리스트를 초기화 하고 인접 정보를 이용하여 작성한다
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        v_1, v_2 = map(int, input().split())
        adj_list[v_1].append(v_2)   # 방향이 있는 그래프임에 주의!

    # start point, goal point 입력
    S, G = map(int, input().split())

    stack = []  # 스택 초기화
    visited = [False] * (V + 1)  # 방문 리스트 초기화
    dfs(S)  # 깊이 우선 탐색 수행

    if G in stack:  # 스택에 goal point가 있다면 길이 있음
        result = 1
    print(f'#{test_case} {result}')
