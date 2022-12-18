# 10157_자리배정

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

C, R = map(int, input().split())
K = int(input())

grid = [[0] * R for _ in range(C)]

x, y = 0, 0
direction = 0
for num in range(1, R * C + 1):
    grid[x][y] = num
    if grid[x][y] == K:
        print(x + 1, y + 1)
        break
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0 <= nx < C and 0 <= ny < R and grid[nx][ny] == 0:
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]

if K > R * C:
    print(0)

