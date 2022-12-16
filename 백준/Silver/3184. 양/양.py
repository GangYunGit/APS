from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    sheep = 0
    wolf = 0
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if yard[i][j] == 'o':
            sheep += 1
        elif yard[i][j] == 'v':
            wolf += 1

        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row and 0 <= check_j < col and not visited[check_i][check_j] and yard[check_i][check_j] != '#':
                visited[check_i][check_j] = True
                queue.append((check_i, check_j))

    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0

    result[0] += sheep
    result[1] += wolf


row, col = map(int, input().split())
yard = [list(input()) for _ in range(row)]
result = [0, 0]

visited = [[False] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if not visited[i][j] and yard[i][j] != '#':
            bfs(i, j)

print(*result)