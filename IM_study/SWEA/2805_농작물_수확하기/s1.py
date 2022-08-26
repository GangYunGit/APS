# 2805_농작물_수확하기

import sys
sys.stdin = open("input.txt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global count
    global revenue
    visited[x][y] = 1
    revenue += farm[x][y]
    queue.append((x, y))

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                revenue += farm[nx][ny]
                queue.append((nx, ny))
        count += 1
        if count == (N // 2 - 1) ** 2 * 2 + 2 * (N // 2 - 1) + 1:
            return


for test_case in range(1, int(input()) + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    start_i, start_j = N // 2, N // 2

    visited = [[0] * N for _ in range(N)]
    queue = []
    count = 0
    revenue = 0
    bfs(start_i, start_j)

    print(f'#{test_case} {revenue}')
