import sys
from collections import deque
input = sys.stdin.readline


# 상 우상 우 우하 하 좌하 좌 좌상
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(i, j):
    global max_depth
    global depth
    visited[i][j] = True
    queue = deque()
    queue.append((i, j, depth))

    while queue:
        if depth > max_depth:
            max_depth = depth
        temp_i, temp_j, depth = queue.popleft()
        if space[temp_i][temp_j] == 1:
            break
        for direction in range(8):
            next_i = temp_i + di[direction]
            next_j = temp_j + dj[direction]
            if 0 <= next_i < row and 0 <= next_j < col and not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                queue.append((next_i, next_j, depth + 1))


row, col = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(row)]
max_depth = 0

for i in range(row):
    for j in range(col):
        if space[i][j] == 0:
            depth = 0
            visited = [[False] * col for _ in range(row)]
            bfs(i, j)
            if depth > max_depth:
                max_depth = depth

print(max_depth)