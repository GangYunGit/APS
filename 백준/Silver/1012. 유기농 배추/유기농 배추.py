import sys

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

        # 지정한 델타 방향의 정점이 ground의 범위 내에 있고,
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and ground[nx][ny] == 1:
            dfs(nx, ny)


T = int(input())
for test_case in range(1, T + 1):
    M, N, K = map(int, input().split())
    earthworm = [list(map(int, input().split())) for _ in range(K)]

    ground = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    earthworm_count = 0

    for b_x, b_y in earthworm:
        ground[b_x][b_y] += 1
    
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and ground[i][j] == 1:
                dfs(i, j)
                earthworm_count += 1

    print(earthworm_count)