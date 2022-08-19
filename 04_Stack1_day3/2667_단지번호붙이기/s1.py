# 2667_단지번호붙이기

import sys
sys.stdin = open("input.txt")


def dfs(x, y):
    global total
    visited[x][y] = True
    total += 1

    # 델타이동
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny)


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []     # 결과값 (단지 내 집의 수들의 모임)

# 이차원리스트를 행 순회
for i in range(N):
    for j in range(N):
        # 아직 방문 안한 집이고, 1이면(집이면) DFS 시작
        if not visited[i][j] and board[i][j] == 1:
            total = 0
            dfs(i, j)
            result.append(total)

result.sort()
print(len(result), *result, sep='\n')
