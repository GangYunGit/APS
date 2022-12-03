import sys
input = sys.stdin.readline

def dfs(row, col):
    global count
    board[row][col] = 100

    if row == N - 1:
        # print(board)
        # print('찾음')
        count += 1
        return

    for i in range(N):
        if i != row:
            board[i][col] += 1

    for j in range(N):
        if j != col:
            board[row][j] += 1

    for dia in range(1, N):
        if row + dia < N and col + dia < N:
            board[row + dia][col + dia] += 1
        if row + dia < N and col - dia >= 0:
            board[row + dia][col - dia] += 1

    # print(board)

    next_row = row + 1
    for next_col in range(N):
        if board[next_row][next_col] == 0:
            dfs(next_row, next_col)
            board[next_row][next_col] -= 100

    for i in range(N):
        if i != row:
            board[i][col] -= 1

    for j in range(N):
        if j != col:
            board[row][j] -= 1

    for dia in range(1, N):
        if row + dia < N and col + dia < N:
            board[row + dia][col + dia] -= 1
        if row + dia < N and col - dia >= 0:
            board[row + dia][col - dia] -= 1


N = int(input())
board = [[0] * N for _ in range(N)]
count = 0
for i in range(N):
    dfs(0, i)
    board = [[0] * N for _ in range(N)]

print(count)