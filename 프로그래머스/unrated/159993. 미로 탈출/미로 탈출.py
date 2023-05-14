from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def find_lever(start_i, start_j, map_info):
    queue = deque()
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    queue.append((start_i, start_j, 0))

    while queue:
        i, j, depth = queue.popleft()
        if map_info[i][j] == "L":
            return (i, j, depth)

        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row_size and 0 <= check_j < col_size and not visited[check_i][check_j] and \
                    map_info[check_i][check_j] != "X":
                visited[check_i][check_j] = True
                queue.append((check_i, check_j, depth + 1))
    return (-1, -1, 0)


def find_exit(start_i, start_j, map_info):
    time = 0
    queue = deque()
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    queue.append((start_i, start_j, 0))

    while queue:
        i, j, depth = queue.popleft()
        if map_info[i][j] == "E":
            return depth

        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < row_size and 0 <= check_j < col_size and not visited[check_i][check_j] and \
                    map_info[check_i][check_j] != "X":
                visited[check_i][check_j] = True
                queue.append((check_i, check_j, depth + 1))
    return -1


def solution(maps):
    global row_size
    global col_size
    col_size = len(maps[0])
    row_size = len(maps)
    start_point_i = 0
    start_point_j = 0
    for i in range(row_size):
        for j in range(col_size):
            if maps[i][j] == "S":
                start_point_i, start_point_j = i, j
    lever_i, lever_j, lever_time = find_lever(start_point_i, start_point_j, maps)

    exit_time = 0
    if lever_i == -1:
        return -1
    else:
        exit_time = find_exit(lever_i, lever_j, maps)
        if exit_time == -1:
            return -1
        else:
            return lever_time + exit_time

