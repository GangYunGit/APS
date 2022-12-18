# BOJ_5212. 지구 온난화

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

row, col = map(int, input().split())
map_info = [list(input()) for _ in range(row)]
sink_point = []
x_point = []

for i in range(row):
    for j in range(col):
        if map_info[i][j] == 'X':
            x_point.append((i, j))
            sink_count = 0
            for direction in range(4):
                check_i = i + di[direction]
                check_j = j + dj[direction]
                if not (0 <= check_i < row and 0 <= check_j < col and map_info[check_i][check_j] == 'X'):
                    sink_count += 1
            if sink_count >= 3:
                sink_point.append((i, j))

for i, j in sink_point:
    x_point.remove((i, j))
    map_info[i][j] = '.'

row_checker = []
col_checker = []
for i, j in x_point:
    row_checker.append(i)
    col_checker.append(j)

for i in range(min(row_checker), max(row_checker) + 1):
    for j in range(min(col_checker), max(col_checker) + 1):
        print(map_info[i][j], end='')
    print()
