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
            next_i = i + di[direction]
            next_j = j + dj[direction]
            if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j] and place[next_i][next_j] > rain:
                visited[next_i][next_j] = True
                queue.append((next_i, next_j))


N = int(input())
place = [list(map(int, input().split())) for _ in range(N)]
sink = []

max_rain = 0
for i in range(N):
    for j in range(N):
        if place[i][j] > max_rain:
            max_rain = place[i][j]

for rain in range(max_rain + 1):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for row in range(N):
        for col in range(N):
            if place[row][col] > rain and not visited[row][col]:
                bfs(row, col)
                count += 1
    sink.append(count)

print(max(sink))
