# 1210_Ladder1

import sys
sys.stdin = open('input.txt')

# 좌 우 상
dx = [0, 0, -1]
dy = [-1, 1, 0]

for test_case in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for x in range(100):
        for y in range(100):
            if ladder[x][y] == 2:
                end_x, end_y = x, y

    while end_x != 0:
        for k in range(3):
            nx = end_x + dx[k]
            ny = end_y + dy[k]

            if 0 <= nx < 100 and 0 <= ny < 100:
                if ladder[nx][ny] == 1:
                    end_x = nx
                    end_y = ny
                    ladder[nx][ny] = 0

    print(f'#{N} {end_y}')