from collections import deque
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            check_i = (i + di[direction] + n) % n
            check_j = (j + dj[direction] + m) % m
            if 0 <= check_i < n and 0 <= check_j < m:
                if not visited[check_i][check_j] and planet[check_i][check_j] == 0:
                    visited[check_i][check_j] = True
                    queue.append((check_i, check_j))


n, m = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if planet[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)