di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

n = int(input())
moves = input()
board = [['#'] * 100 for _ in range(100)]

direction = 0
start_idx = 0
for i in range(n):
    if moves[i] == 'L':
        direction = (direction + 3) % 4
    elif moves[i] == 'R':
        direction = (direction + 1) % 4
    else:
        start_idx = i
        break

si, sj = 50, 50
row_min, row_max = 50, 50
col_min, col_max = 50, 50
board[si][sj] = '.'
for moves_idx in range(start_idx, n):
    if moves[moves_idx] == 'L':
        direction = (direction + 3) % 4
    elif moves[moves_idx] == 'R':
        direction = (direction + 1) % 4
    else:
        si += di[direction]
        sj += dj[direction]
        row_min, row_max = min(row_min, si), max(row_max, si)
        col_min, col_max = min(col_min, sj), max(col_max, sj)
        board[si][sj] = '.'

for row in range(row_min, row_max + 1):
    for col in range(col_min, col_max + 1):
        print(board[row][col], end='')
    print()