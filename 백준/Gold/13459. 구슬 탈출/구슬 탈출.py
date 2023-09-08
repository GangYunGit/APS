import sys
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def move_ball(i, j, direction):
    count = 0
    while True:
        if board[i][j] == 'O':
            break

        if board[i + di[direction]][j + dj[direction]] != '#':
            count += 1
            i += di[direction]
            j += dj[direction]
        else:
            break
    return count, i, j


def bfs(red_i, red_j, blue_i, blue_j):
    visited = [[[[False] * col_size for _ in range(row_size)] for _ in range(col_size)] for _ in range(row_size)]
    queue = deque()
    queue.append((red_i, red_j, blue_i, blue_j, 0))
    visited[red_i][red_j][blue_i][blue_j] = True

    while queue:
        red_i, red_j, blue_i, blue_j, count = queue.popleft()
        if count > 10:
            break

        if board[blue_i][blue_j] == 'O':
            continue
        else:
            if board[red_i][red_j] == 'O':
                return 1

        for direction in range(4):
            red_move_count, after_red_move_i, after_red_move_j = move_ball(red_i, red_j, direction)
            blue_move_count, after_blue_move_i, after_blue_move_j = move_ball(blue_i, blue_j, direction)
            if after_red_move_i == after_blue_move_i and after_red_move_j == after_blue_move_j:
                if board[after_red_move_i][after_red_move_j] != 'O':
                    if red_move_count > blue_move_count:
                        after_red_move_i -= di[direction]
                        after_red_move_j -= dj[direction]
                    else:
                        after_blue_move_i -= di[direction]
                        after_blue_move_j -= dj[direction]

            if not visited[after_red_move_i][after_red_move_j][after_blue_move_i][after_blue_move_j]:
                visited[after_red_move_i][after_red_move_j][after_blue_move_i][after_blue_move_j] = True
                queue.append((after_red_move_i, after_red_move_j, after_blue_move_i, after_blue_move_j, count + 1))

    return 0


input = sys.stdin.readline
row_size, col_size = map(int, input().split())
board = [list(input()) for _ in range(row_size)]

red_i, red_j, blue_i, blue_j = 0, 0, 0, 0
for i in range(row_size):
    for j in range(col_size):
        if board[i][j] == 'R':
            red_i, red_j = i, j
        if board[i][j] == 'B':
            blue_i, blue_j = i, j

print(bfs(red_i, red_j, blue_i, blue_j))