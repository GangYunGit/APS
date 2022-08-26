# 1974_스도쿠_검증

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    check = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
    wrong = 0
    result = 0

    for i in range(9):
        row_check = 1
        col_check = 1
        for j in range(9):
            row_check *= board[i][j]
            col_check *= board[j][i]

        if row_check != check or col_check != check:
            wrong += 1
            break

    for k_i in range(0, 9, 3):
        for k_j in range(0, 9, 3):
            square_check = 1
            for i in range(3):
                for j in range(3):
                    square_check *= board[k_i + i][k_j + j]

            if square_check != check:
                wrong += 1
                break

    if wrong == 0:
        result = 1

    print(f'#{test_case} {result} {wrong}')






