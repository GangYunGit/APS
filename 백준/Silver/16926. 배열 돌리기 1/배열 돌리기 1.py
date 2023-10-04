import sys
input = sys.stdin.readline


def rotate(row_start, row_end, col_start, col_end, board, new_board):

    if min(row_end - row_start, col_end - col_start) > 0:
        rotate(row_start + 1, row_end - 1, col_start + 1, col_end - 1, board, new_board)
    else:
        return

    for row in range(row_start, row_end):
        new_board[row + 1][col_start] = board[row][col_start]
    for row in range(row_end, row_start, -1):
        new_board[row - 1][col_end] = board[row][col_end]

    for col in range(col_start, col_end):
        new_board[row_end][col + 1] = board[row_end][col]
    for col in range(col_end, col_start, -1):
        new_board[row_start][col - 1] = board[row_start][col]


n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for _ in range(r):
    new_board = [[0] * m for _ in range(n)]
    rotate(0, n - 1, 0, m - 1, board, new_board)
    board = new_board

for i in range(n):
    print(*board[i])