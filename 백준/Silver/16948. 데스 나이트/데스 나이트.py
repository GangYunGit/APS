from collections import deque

di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]


def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    depth = 0
    queue.append((i, j, depth))

    while queue:
        i, j, depth = queue.popleft()
        if i == r2 and j == c2:
            return depth
        for direction in range(6):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < N and 0 <= check_j < N and not visited[check_i][check_j]:
                visited[check_i][check_j] = True
                queue.append((check_i, check_j, depth + 1))

    return -1


N = int(input())
points = list(map(int, input().split()))

visited = [[False] * N for _ in range(N)]
r1, c1, r2, c2 = points

print(bfs(r1, c1))