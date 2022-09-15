# 1219_길찾기

import sys
sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = True  # 방문했다는 표시
    stack.append(v)  # 방문한 지점을 스택에 쌓음

    for next_v in adj_list[v]:  # 인접한 모든 정점에 대하여
        if not visited[next_v]:  # 방문하지 않았다면
            dfs(next_v)  # 인접 정점으로 이동


for test_case in range(1, 11):
    T, E = map(int, input().split())
    edge_info = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]

    # 홀수번째 항 -> 짝수번째 항 : 간선의 방향임에 주의하여 인접 리스트에 append
    for i in range(E):
        adj_list[edge_info[2*i]].append(edge_info[2*i + 1])

    # 방문 리스트, 스택, 결과값 초기화
    visited = [False] * 100
    stack = []
    result = 0

    dfs(0)      # 시작점(A = 0)에서 DFS 수행

    # 스택에 도착점(B = 99)가 있으면 결과를 표시
    if 99 in stack:
        result = 1

    print(f'#{test_case} {result}')
