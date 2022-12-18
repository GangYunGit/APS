# BOJ_10026. 적록색약
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j, color, visited):
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            next_i, next_j = i + di[direction], j + dj[direction]
            if (
                    0 <= next_i < N and 0 <= next_j < N
                    and not visited[next_i][next_j]
                    and grid[next_i][next_j] == color
            ):
                visited[next_i][next_j] = True
                queue.append((next_i, next_j))


N = int(input())
grid = [list(input()) for _ in range(N)]

visited_normal = [[False] * N for _ in range(N)]
visited_red_green = [[False] * N for _ in range(N)]
normal_part_count = 0
red_green_part_count = 0

for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            bfs(i, j, grid[i][j], visited_normal)
            normal_part_count += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if not visited_red_green[i][j]:
            bfs(i, j, grid[i][j], visited_red_green)
            red_green_part_count += 1

print(normal_part_count, red_green_part_count)