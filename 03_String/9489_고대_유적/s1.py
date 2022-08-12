# 9489_고대_유적

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    counter_row = []
    for i in range(N):
        count_1_row = 0
        for j in range(M):
            if grid[i][j] == 1:
                count_1_row += 1
                counter_row.append(count_1_row)
            else:
                count_1_row = 0
                counter_row.append(count_1_row)

    counter_column = []
    for j in range(M):
        count_1_column = 0
        for i in range(N):
            if grid[i][j] == 1:
                count_1_column += 1
                counter_column.append(count_1_column)
            else:
                count_1_column = 0
                counter_column.append(count_1_column)

    print(f'#{test_case} {max(*counter_row, *counter_column)}')






