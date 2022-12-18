# BOJ_1012. 유기농 배추
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            next_i, next_j = i + di[direction], j + dj[direction]
            if 0 <= next_i < row and 0 <= next_j < col and not visited[next_i][next_j] and ground[next_i][next_j] == 1:
                visited[next_i][next_j] = True
                queue.append((next_i, next_j))


for test_case in range(1, int(input()) + 1):
    col, row, bachu = map(int, input().split())
    ground = [[0] * col for _ in range(row)]

    count = 0

    for _ in range(bachu):
        j, i = map(int, input().split())
        ground[i][j] = 1

    visited = [[False] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if ground[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)