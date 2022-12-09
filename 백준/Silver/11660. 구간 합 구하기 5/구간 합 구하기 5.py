import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
start_end_point = [list(map(int, input().split())) for _ in range(M)]

memo = [[0] * N for _ in range(N)]
memo[0][0] = board[0][0]

for row in range(1, N):
    memo[row][0] = memo[row - 1][0] + board[row][0]

for col in range(1, N):
    memo[0][col] = memo[0][col - 1] + board[0][col]

for row in range(1, N):
    memo_col = board[row][0]
    for col in range(1, N):
        memo_col += board[row][col]
        memo[row][col] = memo_col + memo[row - 1][col]

for x1, y1, x2, y2 in start_end_point:

    if x1 < 2 and y1 < 2:
        result = memo[x2 - 1][y2 - 1]
    elif x1 < 2:
        result = memo[x2 - 1][y2 - 1] - memo[x2 - 1][y1 - 2]

    elif y1 < 2:
        result = memo[x2 - 1][y2 - 1] - memo[x1 - 2][y2 - 1]

    else:
        result = memo[x2 - 1][y2 - 1] - memo[x1 - 2][y2 - 1] - memo[x2 - 1][y1 - 2] + memo[x1 - 2][y1 - 2]
    print(result)