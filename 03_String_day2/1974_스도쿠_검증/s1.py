# 1974_스도쿠_검증

import sys

sys.stdin = open('input.txt')

for test_case in range(1, int(input()) + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    row_col_check = 0
    square_check = 0
    result = 0

    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            row_sum += puzzle[i][j]
            col_sum += puzzle[j][i]

        if row_sum == 45 and col_sum == 45:
            row_col_check = 1
        else:
            row_col_check = 0
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square_sum = 0
            for k1 in range(3):
                for k2 in range(3):
                    square_sum += puzzle[i + k1][j + k2]
        if square_sum == 45:
            square_check = 1
        else:
            square_check = 0
            break

    if (row_col_check + square_check) == 2:
        result = 1
    else:
        result = 0
    print(f'#{test_case} {result}')

