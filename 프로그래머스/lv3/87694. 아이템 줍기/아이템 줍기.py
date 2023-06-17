from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def make_square(ld_x, ld_y, ru_x, ru_y, board):
    for i in range(ld_x, ru_x + 1):
        if board[i][ld_y] != 2:
            board[i][ld_y] = 1

    for i in range(ld_x, ru_x + 1):
        if board[i][ru_y] != 2:
            board[i][ru_y] = 1

    for i in range(ld_y, ru_y + 1):
        if board[ld_x][i] != 2:
            board[ld_x][i] = 1

    for i in range(ld_y, ru_y + 1):
        if board[ru_x][i] != 2:
            board[ru_x][i] = 1

    for i in range(ld_x + 1, ru_x):
        for j in range(ld_y + 1, ru_y):
            board[i][j] = 2

    return board

def bfs(i, j, itemX, itemY, board):
    visited = [[False] * 101 for _ in range(101)]
    queue = deque()
    count = 0
    queue.append((i, j, count))
    while queue:
        i, j, count = queue.popleft()
        if (i, j) == (itemX, itemY):
            break
        for direction in range(4):
            ni = i + di[direction]
            nj = j + dj[direction]
            if 0 <= ni < 101 and 0 <= nj < 101 and not visited[ni][nj] and board[ni][nj] == 1:
                visited[ni][nj] = True
                queue.append((ni, nj, count + 1))
    
    return count


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 101 for _ in range(101)]
    answer = 0
    for ld_x, ld_y, ru_x, ru_y in rectangle:
        board = make_square(ld_x * 2, ld_y * 2, ru_x * 2, ru_y * 2, board)
    answer = bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2, board) // 2
    return answer