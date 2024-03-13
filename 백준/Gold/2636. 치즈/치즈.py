from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    visited = [[False] * col for _ in range(row)]
    queue = deque()
    visited[i][j] = True
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if board[i][j] == 1:
            board[i][j] = 0
            continue
        for direction in range(4):
            ni, nj = i + di[direction], j + dj[direction]
            if 0 <= ni < row and 0 <= nj < col and not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append((ni, nj))

    remain_cheese = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                remain_cheese += 1

    return remain_cheese


row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
cheese_info = []

count = 0
for i in range(row):
    for j in range(col):
        if board[i][j] == 1:
            count += 1
if count > 0:
    cheese_info.append(count)

while True:
    remain_cheese = bfs(0, 0)
    if remain_cheese == 0:
        break
    cheese_info.append(remain_cheese)
print(len(cheese_info))
if cheese_info:
    print(cheese_info[-1])
else:
    print(0)
