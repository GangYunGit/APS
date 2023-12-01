di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def shot(i, j, direction):

    ni, nj = i, j
    next_dir = direction
    while True:
        if box[ni][nj] == 1:
            if next_dir == 0:
                next_dir = 1
            elif next_dir == 1:
                next_dir = 0
            elif next_dir == 2:
                next_dir = 3
            else:
                next_dir = 2
        ni += di[next_dir]
        nj += dj[next_dir]
        if not (1 <= ni < n + 1 and 1 <= nj < m + 1):
            break

    return hole[ni][nj]


n, m = map(int, input().split())
hole = [[0] * (m + 2) for _ in range(n + 2)]
box = [[0] * (m + 2) for _ in range(n + 2)]

i, j, d = 1, 0, 2
count = 1
for row in range(n):
    hole[row + 1][0] = count
    count += 1
for col in range(m):
    hole[n + 1][col + 1] = count
    count += 1
for row in range(n - 1, -1, -1):
    hole[row + 1][m + 1] = count
    count += 1
for col in range(m - 1, -1, -1):
    hole[0][col + 1] = count
    count += 1


for row in range(n):
    line = list(map(int, input().split()))
    for col in range(m):
        box[row + 1][col + 1] = line[col]


for row in range(1, n + 1):
    print(shot(row, 1, 1), end=" ")
for col in range(1, m + 1):
    print(shot(n, col, 0), end=" ")
for row in range(n, 0, -1):
    print(shot(row, m, 3), end=" ")
for col in range(m, 0, -1):
    print(shot(1, col, 2), end=" ")