from collections import deque

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            distance[i][j] = 0

si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            si, sj = i, j

queue = deque()
queue.append((si, sj, 0))
visited[si][sj] = True
while queue:
    i, j, d = queue.popleft()
    distance[i][j] = d
    for direction in range(4):
        ni, nj = i + di[direction], j + dj[direction]
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            if board[ni][nj] == 1:
                visited[ni][nj] = True
                queue.append((ni, nj, d + 1))
            elif board[ni][nj] == 0:
                distance[ni][nj] = 0

for i in range(n):
    print(*distance[i])