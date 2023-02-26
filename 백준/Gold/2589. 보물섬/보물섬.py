from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))
    route = []
    while queue:
        i, j = queue.popleft()
        route.append((i, j))
        # print(i, j)
        for direction in range(4):
            next_i = i + di[direction]
            next_j = j + dj[direction]
            if 0 <= next_i < row and 0 <= next_j < col and not visited[next_i][next_j] and treasure_map[next_i][next_j] == "L":
                visited[next_i][next_j] = True
                queue.append((next_i, next_j))

    return route


def find_max_distance(i, j):
    check_visited = [[False] * col for _ in range(row)]
    check_visited[i][j] = True
    queue = deque()
    depth = 0
    queue.append((i, j, depth))

    while queue:
        i, j, depth = queue.popleft()
        for direction in range(4):
            next_i = i + di[direction]
            next_j = j + dj[direction]
            if 0 <= next_i < row and 0 <= next_j < col and not check_visited[next_i][next_j] and treasure_map[next_i][next_j] == "L":
                check_visited[next_i][next_j] = True
                queue.append((next_i, next_j, depth + 1))

    return depth


row, col = map(int, input().split())
treasure_map = [input() for _ in range(row)]
visited = [[False] * col for _ in range(row)]
max_distance = 0

for i in range(row):
    for j in range(col):
        if not visited[i][j] and treasure_map[i][j] == "L":
            for start_i, start_j in bfs(i, j):
                max_distance = max(max_distance, find_max_distance(start_i, start_j))

print(max_distance)
