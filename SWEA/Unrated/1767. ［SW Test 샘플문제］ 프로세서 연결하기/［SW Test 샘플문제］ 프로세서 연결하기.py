di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def connect_core(direction, core_i, core_j):
    ni, nj = core_i + di[direction], core_j + dj[direction]
    while True:
        if not (0 <= ni < n and 0 <= nj < n):
            break
        cell[ni][nj] = 1 - cell[ni][nj]
        ni += di[direction]
        nj += dj[direction]


def dfs(current_core, connection_count, total_length):
    global max_connection_count, min_total_length

    if connection_count > max_connection_count:
        max_connection_count = connection_count
        min_total_length = total_length
    elif connection_count == max_connection_count:
        if total_length < min_total_length:
            min_total_length = total_length

    if current_core == max_core:
        return

    dir_check = [0] * 4
    i, j = core[current_core][0], core[current_core][1]
    for direction in range(4):
        ni, nj = i + di[direction], j + dj[direction]
        length = 0
        while True:
            if not (0 <= ni < n and 0 <= nj < n):
                break

            if cell[ni][nj] == 0:
                length += 1
            else:
                length = 0
                break
            ni += di[direction]
            nj += dj[direction]
        dir_check[direction] = length

    for direction in range(4):
        if dir_check[direction] != 0:
            connect_core(direction, i, j)
            total_length += dir_check[direction]
            dfs(current_core + 1, connection_count + 1, total_length)
            connect_core(direction, i, j)
            total_length -= dir_check[direction]
    dfs(current_core + 1, connection_count, total_length)


for test_case in range(1, int(input()) + 1):
    n = int(input())
    cell = [list(map(int, input().split())) for _ in range(n)]
    core = []
    max_connection_count, min_total_length = 0, 12 * 12
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if cell[i][j] == 1:
                core.append((i, j))
    max_core = len(core)
    dfs(0, 0, 0)
    print(f'#{test_case} {min_total_length}')