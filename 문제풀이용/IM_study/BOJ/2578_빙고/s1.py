# 2578_빙고
import sys
sys.stdin = open("input.txt")

board = [list(map(int, input().split())) for _ in range(5)]
called = [input() for _ in range(5)]
called_nums = ' '.join(called).split()

visited = [[0] * 5 for _ in range(5)]

for num in range(len(called_nums)):
    count = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == int(called_nums[num]):
                visited[i][j] = 1

    for b_i in range(5):
        row_bingo = 0
        for b_j in range(5):
            if visited[b_i][b_j] == 1:
                row_bingo += 1
        if row_bingo == 5:
            count += 1

    for b_i in range(5):
        col_bingo = 0
        for b_j in range(5):
            if visited[b_j][b_i] == 1:
                col_bingo += 1
        if col_bingo == 5:
            count += 1

    cross_bingo_1 = 0
    for b_i in range(5):
        if visited[b_i][b_i] == 1:
            cross_bingo_1 += 1
        if cross_bingo_1 == 5:
            count += 1

    cross_bingo_2 = 0
    for b_i in range(5):
        if visited[b_i][4 - b_i] == 1:
            cross_bingo_2 += 1
        if cross_bingo_2 == 5:
            count += 1

    if count >= 3:
        print(num + 1)
        break
