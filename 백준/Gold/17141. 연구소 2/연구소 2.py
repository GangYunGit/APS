from itertools import combinations
from collections import deque
from copy import deepcopy


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(virus_list):
    all_infected_time = 0
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    for virus in virus_list:
        visited[virus[0]][virus[1]] = True
        copied_lab[virus[0]][virus[1]] = 1
        queue.append((virus[0], virus[1], 1))

    while queue:
        i, j, time = queue.popleft()
        for direction in range(4):
            check_i, check_j = i + di[direction], j + dj[direction]
            if 0 <= check_i < n and 0 <= check_j < n and not visited[check_i][check_j] and not copied_lab[check_i][check_j]:
                visited[check_i][check_j] = True
                copied_lab[check_i][check_j] = 1
                all_infected_time = max(time, all_infected_time)
                queue.append((check_i, check_j, time + 1))

    for i in range(n):
        for j in range(n):
            if not copied_lab[i][j]:
                return -1

    return all_infected_time


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
virus_points = []

for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            lab[i][j] = 0
            virus_points.append((i, j))

INF = 50 * 50
min_time = INF
for virus_list in combinations(virus_points, m):
    copied_lab = deepcopy(lab)
    infected_time = bfs(virus_list)
    if infected_time != -1:
        min_time = min(infected_time, min_time)

if min_time == INF:
    print(-1)
else:
    print(min_time)