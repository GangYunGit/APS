import sys
from collections import deque

# 북 동 남 서 상 하
di = [-1, 0, 1, 0, 0, 0]    # 행
dj = [0, 1, 0, -1, 0, 0]    # 열
dk = [0, 0, 0, 0, -1, 1]    # 층


def escape(i, j, k):
    visited[i][j][k] = True
    queue.append((i, j, k, 0))

    while queue:
        i, j, k, time = queue.popleft()
        if building[i][j][k] == 'E':
            return time

        for direction in range(6):
            ni, nj, nk = i + di[direction], j + dj[direction], k + dk[direction]
            if 0 <= ni < l and 0 <= nj < r and 0 <= nk < c and not visited[ni][nj][nk]:
                if building[ni][nj][nk] == '.' or building[ni][nj][nk] == 'E':
                    visited[ni][nj][nk] = True
                    queue.append((ni, nj, nk, time + 1))

    return -1


input = sys.stdin.readline
while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    visited = [[[False for _1 in range(c)] for _2 in range(r)] for _3 in range(l)]
    queue = deque()
    building = []
    for _ in range(l):
        floor = [" ".join(input()).split() for _ in range(r)]
        building.append(floor)
        input()

    result = 0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    result = escape(i, j, k)

    if result == -1:
        print("Trapped!")
    else:
        print(f'Escaped in {result} minute(s).')