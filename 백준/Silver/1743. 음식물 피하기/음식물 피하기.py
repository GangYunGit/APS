import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(i, j):
    global trash_count
    visited[i][j] = True
    for direction in range(4):
        check_i = i + di[direction]
        check_j = j + dj[direction]
        if 0 <= check_i < row and 0 <= check_j < col and road[check_i][check_j] == 1 and not visited[check_i][check_j]:
            trash_count += 1
            dfs(check_i, check_j)


row, col, trash = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(trash)]

road = [[0] * col for _ in range(row)]
for i, j in points:
    road[i - 1][j - 1] = 1

visited = [[False] * col for _ in range(row)]
max_trash = 0

for i in range(row):
    for j in range(col):
        if road[i][j] == 1 and not visited[i][j]:
            trash_count = 1
            dfs(i, j)
            if trash_count > max_trash:
                max_trash = trash_count

print(max_trash)