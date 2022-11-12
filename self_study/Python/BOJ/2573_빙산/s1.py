# BOJ_2573. 빙산
import sys
from collections import deque

input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    global part
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            next_i, next_j = i + di[direction], j + dj[direction]
            if (
                    0 <= next_i < row and 0 <= next_j < col and
                    not visited[next_i][next_j] and iceberg[next_i][next_j] > 0
            ):
                visited[next_i][next_j] = True
                queue.append((next_i, next_j))

    part += 1


row, col = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(row)]
melt_counter = [[0] * col for _ in range(row)]
part = 0
year = 0

visited = [[False] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if iceberg[i][j] > 0 and not visited[i][j]:
            bfs(i, j)

if part >= 2:
    print(0)
    exit()

while part < 2:
    part = 0
    melted_ice = 0
    melt_counter = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if iceberg[i][j] > 0:
                melted_ice += 1
                for direction in range(4):
                    check_i, check_j = i + di[direction], j + dj[direction]
                    if iceberg[check_i][check_j] == 0:
                        melt_counter[i][j] += 1

    for i in range(row):
        for j in range(col):
            iceberg[i][j] -= melt_counter[i][j]
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0

    visited = [[False] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(i, j)

    year += 1
    # print(iceberg)
    # print(part, melted_ice)
    if part == 0 and melted_ice == 0:
        year = 0
        break

print(year)

'''
5 7
0 0 0 0 0 0 0
0 0 2 4 1 0 0
0 1 0 1 5 0 0
0 5 4 1 2 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 0 0 1 0 0
0 1 1 1 1 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 1 1 1 0 0
0 1 1 1 1 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 1 0 1 1 0 0
0 1 0 1 1 0 0
0 1 0 1 1 0 0
0 0 0 0 0 0 0
'''