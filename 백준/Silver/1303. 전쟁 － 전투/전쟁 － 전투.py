from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j, visited_color):
    power = 0
    visited_color[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        power += 1
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row and 0 <= check_j < col and not visited_color[check_i][check_j]:
                if visited_color == visited_w:
                    if field[check_i][check_j] == 'W':
                        visited_color[check_i][check_j] = True
                        queue.append((check_i, check_j))
                else:
                    if field[check_i][check_j] == 'B':
                        visited_color[check_i][check_j] = True
                        queue.append((check_i, check_j))

    return power ** 2


col, row = map(int, input().split())
field = [list(input()) for _ in range(row)]

visited_w = [[False] * col for _ in range(row)]
visited_b = [[False] * col for _ in range(row)]
power_w = 0
power_b = 0

for i in range(row):
    for j in range(col):
        if field[i][j] == 'W' and not visited_w[i][j]:
            power_w += bfs(i, j, visited_w)
        elif field[i][j] == 'B' and not visited_b[i][j]:
            power_b += bfs(i, j, visited_b)

print(power_w, power_b)