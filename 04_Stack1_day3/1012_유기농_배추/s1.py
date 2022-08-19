# 1012_유기농_배추

import sys
sys.stdin = open("input.txt")

sys.setrecursionlimit(100000)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# DFS 탐색 함수
def dfs(x, y):
    visited[x][y] = True    # 방문한 좌표를 표시

    # 델타 검색
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 지정한 델타 방향의 정점이 ground의 범위 내에 있고, 방문하지 않았고, 배추가 있는 경우
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and ground[nx][ny] == 1:
            dfs(nx, ny)     # 다음 방향의 델타 검색을 수행


T = int(input())
for test_case in range(1, T + 1):
    # M, N, K와 배추의 위치 입력받기
    M, N, K = map(int, input().split())
    cabbage = [list(map(int, input().split())) for _ in range(K)]

    # 땅의 좌표를 0으로 초기화, 방문 리스트 초기화, 지렁이 카운트 초기화
    ground = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    earthworm_count = 0

    # 배추가 있는 좌표를 땅에 1로 표시
    for b_x, b_y in cabbage:
        ground[b_x][b_y] += 1

    # 행 우선 순회
    for i in range(M):
        for j in range(N):

            # 방문하지 않았고, 배추가 심어져있는 땅의 좌표를 만나면 dfs 수행
            if not visited[i][j] and ground[i][j] == 1:
                dfs(i, j)
                earthworm_count += 1    # dfs 가 수행된 곳에 지렁이 배정

    print(earthworm_count)
