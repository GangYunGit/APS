# BOJ_16236. 아기 상어
from collections import deque

# 상 좌 하 우
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]


def bfs(i, j):
    global seconds
    visited = [[False] * space_size for _ in range(space_size)]
    seconds = 0
    visited[i][j] = True
    queue = deque()
    queue.append((i, j, seconds))

    while queue:
        temp_i, temp_j, seconds = queue.popleft()
        for direction in range(4):
            next_i = temp_i + di[direction]
            next_j = temp_j + dj[direction]
            if 0 <= next_i < space_size and 0 <= next_j < space_size and not visited[next_i][next_j]:
                if space[next_i][next_j] <= baby_shark['size']:
                    queue.append((next_i, next_j, seconds + 1))
                    visited[next_i][next_j] = True
                    if 0 < space[next_i][next_j] < baby_shark['size']:
                        space[next_i][next_j] = 0
                        baby_shark['eaten_fish'] += 1
                        baby_shark['total_fish'] += 1
                        visited = [[False] * space_size for _ in range(space_size)]
                        if baby_shark['eaten_fish'] == baby_shark['size']:
                            baby_shark['eaten_fish'] = 0
                            baby_shark['size'] += 1

    if baby_shark['total_fish'] == 0:
        seconds = 0

    return seconds


space_size = int(input())
space = [list(map(int, input().split())) for _ in range(space_size)]
print(space)

baby_shark = {'size': 2, 'eaten_fish': 0, 'total_fish': 0}
seconds = 0

for i in range(space_size):
    for j in range(space_size):
        if space[i][j] == 9:
            print(bfs(i, j))

print(space)
