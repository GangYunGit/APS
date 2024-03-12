from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if i == m - 1:
            return True
        for direction in range(4):
            ni, nj = i + di[direction], j + dj[direction]
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] != 1:
                visited[ni][nj] = True
                grid[ni][nj] = 2
                queue.append((ni, nj))

    return False


m, n = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
is_connected = False
result = 'NO'

for i in range(n):
    if is_connected:
        result = 'YES'
        break
    if grid[0][i] == 0 and not visited[0][i]:
        is_connected = bfs(0, i)

print(result)