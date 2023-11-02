def eat_candy():
    max_count = 0
    for row in range(n):
        count = 1
        for col in range(n - 1):
            if board[row][col] == board[row][col + 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)


    for col in range(n):
        count = 1
        for row in range(n - 1):
            if board[row][col] == board[row + 1][col]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count


def change_row(row_idx, col_idx):
    board[row_idx][col_idx], board[row_idx + 1][col_idx] = board[row_idx + 1][col_idx], board[row_idx][col_idx]


def change_col(row_idx, col_idx):
    board[row_idx][col_idx], board[row_idx][col_idx + 1] = board[row_idx][col_idx + 1], board[row_idx][col_idx]


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
max_count = 0

for i in range(n - 1):
    for j in range(n):
        if board[i][j] != board[i + 1][j]:
            change_row(i, j)
            max_count = max(eat_candy(), max_count)
            change_row(i, j)

for j in range(n - 1):
    for i in range(n):
        if board[i][j] != board[i][j + 1]:
            change_col(i, j)
            max_count = max(eat_candy(), max_count)
            change_col(i, j)

print(max_count)