from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(final_second):
    virus_points = []
    for i in range(n):
        for j in range(n):
            if grid_info[i][j] != 0:
                virus_points.append((0, grid_info[i][j], i, j))
    virus_points.sort()

    queue = deque(virus_points)
    while queue:
        second, virus, i, j = queue.popleft()
        if second == final_second:
            break
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < n and 0 <= check_j < n and grid_info[check_i][check_j] == 0:
                grid_info[check_i][check_j] = virus
                queue.append((second + 1, virus, check_i, check_j))


n, k = map(int, input().split())
grid_info = [list(map(int, input().split())) for _ in range(n)]
seconds, x, y = map(int, input().split())
bfs(seconds)
print(grid_info[x - 1][y - 1])