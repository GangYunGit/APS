from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def chose_infect(start, end):
    global min_infected
    pick_length = len(pick)

    if pick_length == end:
        for i, j in pick:
            map_info[i][j] = 1

        infected_count = 0
        visited_infect = [[False] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if map_info[i][j] == 2 and not visited_infect[i][j]:
                    infected_count += bfs(i, j, visited_infect)
        min_infected = min(infected_count, min_infected)

        return

    for i in range(start, len(not_infected)):
        pick.append(not_infected[i])
        chose_infect(i + 1, end)
        p_i, p_j = pick.pop()
        map_info[p_i][p_j] = 0


def bfs(i, j, visited_infect):
    global map_info
    infect_count = 0

    visited_infect[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if map_info[i][j] == 0:
            infect_count += 1
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if (
                    0 <= check_i < row and 0 <= check_j < col
                    and not visited_infect[check_i][check_j]
                    and (map_info[check_i][check_j] == 0 or map_info[check_i][check_j] == 2)
            ):
                visited_infect[check_i][check_j] = True
                queue.append((check_i, check_j))

    return infect_count


row, col = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(row)]
not_infected = []

for i in range(row):
    for j in range(col):
        if map_info[i][j] == 0:
            not_infected.append((i, j))

pick = []
not_infected_total = len(not_infected) - 3
count = 0
min_infected = not_infected_total
chose_infect(0, 3)
print(not_infected_total - min_infected)