from collections import deque

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    visited = [[False] * m for _ in range(n)]
    count = 1
    queue = deque()
    queue.append((i, j, left, right))
    visited[i][j] = True

    while queue:
        i, j, left_count, right_count = queue.popleft()
        for direction in range(2):
            ni, nj = i + di[direction], j + dj[direction]
            while 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == 0:
                count += 1
                visited[ni][nj] = True
                queue.append((ni, nj, left_count, right_count))
                ni, nj = ni + di[direction], nj + dj[direction]

        if left_count > 0:
            ni, nj = i + di[2], j + dj[2]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == 0:
                count += 1
                visited[ni][nj] = True
                queue.append((ni, nj, left_count - 1, right_count))
        if right_count > 0:
            ni, nj = i + di[3], j + dj[3]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == 0:
                count += 1
                visited[ni][nj] = True
                queue.append((ni, nj, left_count, right_count - 1))

    return count


n, m = map(int, input().split())
left, right = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            si, sj = i, j
            board[i][j] = 0
            break
print(bfs(si, sj))