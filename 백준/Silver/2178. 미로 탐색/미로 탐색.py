from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    depth = 1
    visited[i][j] = depth
    queue = deque()
    queue.append((i, j, depth))

    while queue:
        temp_i, temp_j, depth = queue.popleft()
        depth += 1
        for direction in range(4):
            next_i = temp_i + di[direction]
            next_j = temp_j + dj[direction]
            if 0 <= next_i < N and 0 <= next_j < M and visited[next_i][next_j] == 0 and maze[next_i][next_j] == '1':
                visited[next_i][next_j] = depth
                queue.append((next_i, next_j, depth))


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
bfs(0, 0)
print(visited[N - 1][M - 1])