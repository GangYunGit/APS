# BOJ_15686. 치킨 배달
import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    global depth
    visited[i][j] = True
    queue = deque()
    queue.append((i, j, depth))

    while queue:
        temp_i, temp_j, depth = queue.popleft()
        if (temp_i, temp_j) == bbq:
            # print(depth)
            break
        for direction in range(4):
            next_i, next_j = temp_i + di[direction], temp_j + dj[direction]
            if 0 <= next_i < city_size and 0 <= next_j < city_size and not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                queue.append((next_i, next_j, depth + 1))


city_size, alive_BBQ = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(city_size)]

bbq_list = []
picked = []
combs = []
chicken_distance_list = []
min_chicken_distance = 100 * 13

for i in range(city_size):
    for j in range(city_size):
        if city_info[i][j] == 2:
            bbq_list.append((i, j))


for bbq in bbq_list:
    chicken_distance = 0
    for i in range(city_size):
        for j in range(city_size):
            if city_info[i][j] == 1:
                visited = [[False] * city_size for _ in range(city_size)]
                depth = 0
                bfs(i, j)
                chicken_distance += depth
    print(chicken_distance)

