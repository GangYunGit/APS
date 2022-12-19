from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j, count):
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row and 0 <= check_j < col and not visited[check_i][check_j] and grid[check_i][check_j] == 0:
                count += 1
                visited[check_i][check_j] = True
                queue.append((check_i, check_j))

    return count


row, col, k = map(int, input().split())
square_points = [list(map(int, input().split())) for _ in range(k)]

grid = [[0] * col for _ in range(row)]

for x1, y1, x2, y2 in square_points:
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

visited = [[False] * col for _ in range(row)]
result = []
region = 0
for i in range(row):
    for j in range(col):
        if not visited[i][j] and grid[i][j] == 0:
            region += 1
            result.append(bfs(i, j, count=1))

print(region)
print(*sorted(result))