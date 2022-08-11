# 4836_색칠하기

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]
    count = 0

    for _ in range(N):
        x_start, y_start, x_end, y_end, color = map(int,input().split())

        if color == 1:
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    grid[i][j] += 1

        if color == 2:
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    grid[i][j] += 10

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 11:
                count += 1

    print(f'#{test_case} {count}')

