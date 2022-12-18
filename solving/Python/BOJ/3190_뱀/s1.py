# BOJ_3190. 뱀
from collections import deque

N = int(input())
K = int(input())
apple_points = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
snake_directions = deque(list(input().split()) for _ in range(L))

# 뱀 : 1, 사과 : 2
di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]
board = [[0] * N for _ in range(N)]
for apple in apple_points:
    board[apple[0] - 1][apple[1] - 1] = 2

direction = 0
board[0][0] = 1
body = deque()
body.append((0, 0))
next_i, next_j = di[direction], dj[direction]
if board[next_i][next_j] != 2:
    tail_i, tail_j = body.popleft()
    board[tail_i][tail_j] = 0
board[next_i][next_j] = 1
body.append((next_i, next_j))
count = 0
i, j = next_i, next_j
while True:
    count += 1
    if snake_directions and count == int(snake_directions[0][0]):
        next_direction = snake_directions.popleft()[1]
        if next_direction == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4

    next_i, next_j = i + di[direction], j + dj[direction]
    # 범위를 벗어나거나 뱀을 만나면 탈출
    if not(0 <= next_i < N and 0 <= next_j < N) or board[next_i][next_j] == 1:
        count += 1
        break

    if board[next_i][next_j] != 2:
        tail_i, tail_j = body.popleft()
        board[tail_i][tail_j] = 0

    board[next_i][next_j] = 1
    body.append((next_i, next_j))

    i, j = next_i, next_j
print(count)



