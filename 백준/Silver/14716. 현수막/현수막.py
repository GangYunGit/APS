from collections import deque


di = [1, 0, -1, 0, 1, 1, -1, -1]
dj = [0, 1, 0, -1, 1, -1, 1, -1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        for direction in range(8):
            check_i, check_j = i + di[direction], j + dj[direction]
            if 0 <= check_i < m and 0 <= check_j < n and banner[check_i][check_j] and not visited[check_i][check_j]:
                visited[check_i][check_j] = True
                queue.append((check_i, check_j))


m, n = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
count = 0

for row in range(m):
    for col in range(n):
        if banner[row][col] and not visited[row][col]:
            visited[row][col] = True
            bfs(row, col)
            count += 1

print(count)