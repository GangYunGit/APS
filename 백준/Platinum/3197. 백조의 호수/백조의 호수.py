import sys
from collections import deque

input = sys.stdin.readline
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def first_melt_checker(i, j):
    visited_ice[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row and 0 <= check_j < col and not visited_ice[check_i][check_j]:
                visited_ice[check_i][check_j] = True
                if lake[check_i][check_j] == 'X':
                    melt_points.append((check_i, check_j))
                    continue
                queue.append((check_i, check_j))


def melt_and_next_points(melt_list):
    next_list = deque()
    for i, j in melt_list:
        lake[i][j] = '.'
        visited_ice[i][j] = False

    for i, j in melt_list:
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row and 0 <= check_j < col and not visited_ice[check_i][check_j] and lake[check_i][check_j] == 'X':
                visited_ice[check_i][check_j] = True
                next_list.append((check_i, check_j))
    return next_list


def bfs_swan(queue):
    global swan_count
    next_list = deque()

    for i, j in queue:
        visited_swan[i][j] = True

    while queue:
        i, j = queue.popleft()
        if lake[i][j] == 'L':
            swan_count += 1
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row and 0 <= check_j < col and not visited_swan[check_i][check_j]:
                visited_swan[check_i][check_j] = True
                if lake[check_i][check_j] == 'X':
                    next_list.append((check_i, check_j))
                    continue
                queue.append((check_i, check_j))

    return next_list


row, col = map(int, input().split())
lake = [list(input()) for _ in range(row)]
visited_ice = [[False] * col for _ in range(row)]

melt_points = deque()
for i in range(row):
    for j in range(col):
        if not visited_ice[i][j] and lake[i][j] != 'X':
            first_melt_checker(i, j)

swan_count = 0
visited_swan = [[False] * col for _ in range(row)]

tmp = []
for i in range(row):
    for j in range(col):
        if lake[i][j] == 'L':
            tmp.append((i, j))
tmpdeque = deque()
tmpdeque.append(tmp[0])
blocked_points = bfs_swan(tmpdeque)

result = 0

while True:
    new_points = melt_and_next_points(melt_points)
    new_blocked_points = bfs_swan(blocked_points)
    melt_points = new_points
    blocked_points = new_blocked_points
    result += 1
    if swan_count == 2:
        break

print(result)