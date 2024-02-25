n = int(input())
cookie = [list(input().rstrip()) for _ in range(n)]

heart_i, heart_j = 0, 0
result = [0, 0, 0, 0, 0]

# 심장 위치
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            heart_i, heart_j = i + 1, j
    if heart_j > 0:
        break

# 왼팔 위치
x, y = heart_i, heart_j
count = 0
while True:
    y -= 1
    if 0 <= y < n and cookie[x][y] == '*':
        count += 1
    else:
        result[0] = count
        break

# 오른팔 위치
x, y = heart_i, heart_j
count = 0
while True:
    y += 1
    if 0 <= y < n and cookie[x][y] == '*':
        count += 1
    else:
        result[1] = count
        break

# 허리 위치
x, y = heart_i, heart_j
x_end, y_end = 0, heart_j
count = 0
while True:
    x += 1
    if 0 <= x < n and cookie[x][y] == '*':
        count += 1
    else:
        result[2] = count
        x_end, y_end = x - 1, heart_j
        break

# 왼쪽 다리 위치
x, y = x_end + 1, y_end - 1
count = 1
while True:
    x += 1
    if 0 <= x < n and cookie[x][y] == '*':
        count += 1
    else:
        result[3] = count
        break

# 오른쪽 다리 위치
x, y = x_end + 1, y_end + 1
count = 1
while True:
    x += 1
    if 0 <= x < n and cookie[x][y] == '*':
        count += 1
    else:
        result[4] = count
        break

print(heart_i + 1, heart_j + 1)
print(*result)