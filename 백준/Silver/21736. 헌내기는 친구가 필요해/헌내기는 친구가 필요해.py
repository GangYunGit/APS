from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    queue.append((i, j))
    visited[i][j] = True
    count = 0

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            ni, nj = i + di[direction], j + dj[direction]
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if not visited[ni][nj] and campus[ni][nj] != 'X':
                visited[ni][nj] = True
                if campus[ni][nj] == 'P':
                    count += 1
                queue.append((ni, nj))

    return count


n, m = map(int, input().split())
campus = [list(input().strip()) for _ in range(n)]
si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            si, sj = i, j

result = bfs(si, sj)
if result == 0:
    print('TT')
else:
    print(result)