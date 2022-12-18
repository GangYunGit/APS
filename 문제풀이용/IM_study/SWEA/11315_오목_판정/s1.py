# 11315_오목판정

import sys
sys.stdin = open("input.txt")

# 우 우하 하 좌하
dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

for test_case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    counter = [[0] * N for _ in range(N)]
    result = 'NO'

    for direction in range(4):
        for x in range(N):
            for y in range(N):
                count = 0
                if board[x][y] == 'o':
                    nx = x
                    ny = y
                    count += 1
                    for k in range(N):
                        nx = nx + dx[direction]
                        ny = ny + dy[direction]
                        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                            count += 1
                        else:
                            break
                    counter[x][y] = count
        for i in range(N):
            for j in range(N):
                if counter[i][j] >= 5:
                    result = 'YES'

    print(f'#{test_case} {result}')