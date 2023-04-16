import sys
from collections import deque
input = sys.stdin.readline


def inner_check(i, j):
    visited[i][j] = True
    grid[i][j] = 2
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            next_i = i + di[direction]
            next_j = j + dj[direction]
            if 0 <= next_i < row and 0 <= next_j < col and not visited[next_i][next_j] and grid[next_i][next_j] != 1:
                visited[next_i][next_j] = True
                grid[next_i][next_j] = 2
                queue.append((next_i, next_j))


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

row, col = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row)]
result = 0
escape_counter = 0
visited = [[False] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        if grid[i][j] == 1:
            escape_counter += 1
            break

inner_check(0, 0)
# print(grid)

while escape_counter != 0:
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                melt_count = 0
                for direction in range(4):
                    check_i = i + di[direction]
                    check_j = j + dj[direction]
                    if grid[check_i][check_j] == 2:
                        melt_count += 1
                    if melt_count >= 2:
                        grid[i][j] = 0
                        break

    result += 1
    visited = [[False] * col for _ in range(row)]
    inner_check(0, 0)
    # for i in range(row):
    #     for j in range(col):
    #         if grid[i][j] == 0:
    #             inner_check(i, j)

    escape_counter = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                escape_counter += 1
                break

print(result)