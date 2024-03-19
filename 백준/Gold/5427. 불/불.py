from collections import deque
import sys

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    visited_escape = [[False] * col for _ in range(row)]
    queue_escape = deque()
    time = 0
    queue_escape.append((i, j))
    visited_escape[i][j] = True

    visited_fire = [[False] * col for _ in range(row)]
    queue_fire = deque()
    for i in range(row):
        for j in range(col):
            if building[i][j] == '*':
                queue_fire.append((i, j))
                visited_fire[i][j] = True

    while queue_escape:
        time += 1
        # print(*building, sep="\n")
        # print()
        temp_points_fire = []
        while queue_fire:
            fi, fj = queue_fire.popleft()
            for direction in range(4):
                ni, nj = fi + di[direction], fj + dj[direction]
                if not(0 <= ni < row and 0 <= nj < col):
                    continue
                if not visited_fire[ni][nj] and building[ni][nj] != '#':
                    visited_fire[ni][nj] = True
                    building[ni][nj] = '*'
                    temp_points_fire.append((ni, nj))
        for i, j in temp_points_fire:
            queue_fire.append((i, j))

        temp_points_escape = []
        while queue_escape:
            ei, ej = queue_escape.popleft()
            for direction in range(4):
                ni, nj = ei + di[direction], ej + dj[direction]
                if not(0 <= ni < row and 0 <= nj < col):
                    return time
                if not visited_escape[ni][nj] and (building[ni][nj] == '.' or building[ni][nj] == '@'):
                    visited_escape[ni][nj] = True
                    temp_points_escape.append((ni, nj))

        for i, j in temp_points_escape:
            queue_escape.append((i, j))

    return -1


input = sys.stdin.readline
for _ in range(int(input())):
    col, row = map(int, input().split())
    building = [list(input().strip()) for _ in range(row)]
    result = 0
    for i in range(row):
        for j in range(col):
            if building[i][j] == '@':
                result = bfs(i, j)
                if result == -1:
                    print('IMPOSSIBLE')
                else:
                    print(result)
                break