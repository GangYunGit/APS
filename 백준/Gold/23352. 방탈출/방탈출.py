import sys
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    queue = deque()
    count = 0
    queue.append((i, j, 0))
    si, sj, ei, ej = i, j, i, j

    while queue:
        i, j, length = queue.popleft()
        count = length
        for direction in range(4):
            ni, nj = i + di[direction], j + dj[direction]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and room[ni][nj] != 0:
                visited[ni][nj] = True
                ei, ej = ni, nj
                queue.append((ni, nj, length + 1))

    get_password = room[si][sj] + room[ei][ej]

    return get_password, count


input = sys.stdin.readline
n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
password = 0
max_count = 0

for i in range(n):
    for j in range(m):
        if room[i][j] != 0:
            get_password, count = bfs(i, j)
            if count > max_count:
                password = get_password
                max_count = count
            elif count == max_count:
                if get_password > password:
                    password = get_password

print(password)