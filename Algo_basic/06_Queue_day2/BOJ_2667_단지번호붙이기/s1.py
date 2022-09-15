# BOJ_2667_단지번호붙이기

import sys
sys.stdin = open("input.txt")


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    visited[x][y] = 1
    queue = [(x, y)]
    count = 1

    while queue:
        tx, ty = queue.pop()
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and square[nx][ny] == '1':
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1

    return count


N = int(input())
square = [input() for _ in range(N)]
depart = []
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if square[i][j] == '1' and not visited[i][j]:
            depart.append(bfs(i, j))

depart.sort()
print(len(depart))
print(*depart, sep='\n')

