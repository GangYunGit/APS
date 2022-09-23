# 1953_탈주범_검거

import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def tunnel_type(x, y):
    if tunnel_map[x][y] == 1:
        return 0, 1, 2, 3
    elif tunnel_map[x][y] == 2:
        return 0, 2
    elif tunnel_map[x][y] == 3:
        return 1, 3
    elif tunnel_map[x][y] == 4:
        return 0, 1
    elif tunnel_map[x][y] == 5:
        return 1, 2
    elif tunnel_map[x][y] == 6:
        return 2, 3
    elif tunnel_map[x][y] == 7:
        return 0, 3


def bfs(x, y):
    count = 0
    visited[x][y] = 1
    queue.append((x, y, count + 1))

    while queue:
        x, y, count = queue.pop(0)
        if count == escape_time:
            break
        if tunnel_map[x][y] != 0:
            for direction in tunnel_type(x, y):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < N and 0 <= ny < M and tunnel_map[nx][ny] != 0 and ((direction + 2) % 4) in tunnel_type(nx, ny) and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count + 1))


for test_case in range(1, int(input()) + 1):
    N, M, hole_row, hole_col, escape_time = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    queue = []
    count = 0
    result = 0

    bfs(hole_row, hole_col)

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                result += 1
    print(f'#{test_case} {result}')