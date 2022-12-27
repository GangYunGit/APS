from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j, count):
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        count += 1
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row and 0 <= check_j < col and not visited[check_i][check_j] and paper[check_i][check_j] == 1:
                visited[check_i][check_j] = True
                queue.append((check_i, check_j))

    return count


row, col = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(row)]

visited = [[False] * col for _ in range(row)]
picture = 0
max_width = 0
for i in range(row):
    for j in range(col):
        if paper[i][j] == 1 and not visited[i][j]:
            picture += 1
            max_width = max(bfs(i, j, 0), max_width)

print(picture)
print(max_width)