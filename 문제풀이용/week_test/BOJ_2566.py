# 2566_최대값

board = [list(map(int, input().split())) for _ in range(9)]
row_max = 0
real_max = 0

for i in range(9):
    for j in range(9):
        if board[i][j] > row_max:
            row_max = board[i][j]
    if row_max > real_max:
        real_max = row_max

for i in range(9):
    for j in range(9):
        if board[i][j] == real_max:
            max_row_idx = i + 1
            max_col_idx = j + 1
            break

print(real_max)
print(max_row_idx, max_col_idx)