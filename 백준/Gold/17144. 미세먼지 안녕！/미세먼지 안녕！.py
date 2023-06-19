from copy import deepcopy

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dirt_diffusion():
    for i in range(r):
        for j in range(c):
            if room[i][j] != 0 and room[i][j] != -1:
                remain_dirt = room[i][j]
                diffused_dirt = room[i][j] // 5
                for direction in range(4):
                    ni = i + di[direction]
                    nj = j + dj[direction]
                    if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                        remain_dirt -= diffused_dirt
                        dirt_diffused_room[ni][nj] += diffused_dirt
                dirt_diffused_room[i][j] += remain_dirt


def air_cleaner(up_i, up_j, down_i, down_j):
    for j in range(1, c - 1):       # 오른쪽
        cleaned_room[up_i][j + 1] = room[up_i][j]

    for i in range(1, up_i + 1):    # 위
        cleaned_room[i - 1][c - 1] = room[i][c - 1]

    for j in range(c - 1):          # 왼쪽
        cleaned_room[0][j] = room[0][j + 1]

    for i in range(up_i - 1):       # 아래
        cleaned_room[i + 1][0] = room[i][0]

    #############

    for j in range(1, c - 1):       # 오른쪽
        cleaned_room[down_i][j + 1] = room[down_i][j]

    for i in range(down_i, r - 1):       # 아래
        cleaned_room[i + 1][c - 1] = room[i][c - 1]

    for j in range(c - 1):          # 왼쪽
        cleaned_room[r - 1][j] = room[r - 1][j + 1]

    for i in range(down_i + 2, r):    # 위
        cleaned_room[i - 1][0] = room[i][0]

    for i in range(r):
        for j in range(c):
            if i != 0 and i != up_i and i != down_i and i != r - 1:
                if j != 0 and j != up_j and j != down_j and j != c - 1:
                    cleaned_room[i][j] = room[i][j]


r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

for _ in range(t):
    dirt_diffused_room = [[0] * c for _ in range(r)]
    cleaned_room = [[0] * c for _ in range(r)]
    up_i, up_j, down_i, down_j = 0, 0, 0, 0
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                if up_i == 0 and up_j == 0:
                    up_i, up_j = i, j
                else:
                    down_i, down_j = i, j
                dirt_diffused_room[i][j] = -1
                cleaned_room[i][j] = -1
    dirt_diffusion()
    room = dirt_diffused_room
    air_cleaner(up_i, up_j, down_i, down_j)
    room = deepcopy(cleaned_room)

print(sum(list(map(sum, room))) + 2)