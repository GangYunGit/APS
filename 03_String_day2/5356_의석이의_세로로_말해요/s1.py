# 5356_의석이의_세로로_말해요

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    board = [[0] * 15 for _ in range(5)]
    my_board = [input() for _ in range(5)]
    new_string = ''

    for i in range(5):
        for j in range(len(my_board[i])):
            board[i][j] = my_board[i][j]

    for i in range(15):
        for j in range(5):
            if board[j][i] != 0:
                new_string += board[j][i]

    print(f'#{test_case} {new_string}')


