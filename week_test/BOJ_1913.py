# 1913_달팽이

N = int(input())
find = int(input())
board = [[0] * N for _ in range(N)]

# 좌 하 우 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 출발점 (N x N 행렬의 정 가운데)
nx = N // 2
ny = N // 2
board[nx][ny] = 1
direction = 0
count = 0
num = 0
find_x, find_y = 0, 0

while num != N * N:
    if direction % 2 == 0:
        count += 1

    for _ in range(count):
        num += 1
        nx += dx[direction]
        ny += dy[direction]
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] = num + 1
    direction += 1

    if direction == 4:
        direction = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == find:
            find_x, find_y = i + 1, j + 1

for num in board:
    print(*num)
print(find_x, find_y)