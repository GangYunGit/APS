# 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 1번 : 우 / 2번 : 좌, 우 / 3번 : 상, 우 / 4번 : 좌, 상, 우 / 5번 : 전부
cctv_type = {
    1: [[0], [1], [2], [3]],
    2: [[1, 3], [0, 2]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [1, 2, 0], [2, 3, 1], [3, 0, 2]],
    5: [[0, 1, 2, 3]]
}


def dfs(cctv_location, cctv_idx):
    global min_count
    if cctv_idx == len(cctv_location):
        count = 0
        for i in range(n):
            for j in range(m):
                if room[i][j] == 0:
                    count += 1
        min_count = min(min_count, count)
        return

    cctv_i, cctv_j = cctv_location[cctv_idx]
    for direction_list in cctv_type[room[cctv_i][cctv_j]]:
        checked_area = []
        for direction in direction_list:
            k = 1
            while True:
                check_i, check_j = cctv_i + k * di[direction], cctv_j + k * dj[direction]
                if not (0 <= check_i < n and 0 <= check_j < m):
                    break
                else:
                    if room[check_i][check_j] == 6:
                        break
                    elif room[check_i][check_j] == 0:
                        room[check_i][check_j] = -1
                        checked_area.append((check_i, check_j))
                    k += 1

        dfs(cctv_location, cctv_idx + 1)
        for row, col in checked_area:
            room[row][col] = 0


n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cctv_location = []

for row in range(n):
    for col in range(m):
        if 0 < room[row][col] < 6:
            cctv_location.append((row, col))

min_count = n * m
cctv_rotation = []
dfs(cctv_location, 0)
print(min_count)