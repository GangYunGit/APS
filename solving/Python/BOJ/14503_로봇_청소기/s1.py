# BOJ_14503. 로봇 청소기

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(i, j, now_direction):
    global cleaned
    if room[i][j] == 0:
        room[i][j] = 2
        cleaned += 1

    cleaned_or_wall = 0
    for direction in range(4):
        next_i, next_j = i + di[direction], j + dj[direction]
        if room[next_i][next_j] == 1 or room[next_i][next_j] == 2:
            cleaned_or_wall += 1

    if cleaned_or_wall == 4:
        next_direction = (now_direction + 2) % 4
        next_i, next_j = i + di[next_direction], j + dj[next_direction]
        if room[next_i][next_j] == 1:
            print(cleaned)
            return
        else:
            dfs(next_i, next_j, now_direction)
    else:
        next_direction = (4 + now_direction - 1) % 4
        next_i, next_j = i + di[next_direction], j + dj[next_direction]
        if room[next_i][next_j] == 0:
            cleaned += 1
            room[next_i][next_j] = 2
            dfs(next_i, next_j, next_direction)
        else:
            dfs(i, j, next_direction)


N, M = map(int, input().split())
now_i, now_j, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cleaned = 0

dfs(now_i, now_j, d)
