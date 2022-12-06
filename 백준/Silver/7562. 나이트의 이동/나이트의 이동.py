from collections import deque

di = [2, 1, -1, -2, -2, -1, 1, 2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    depth = 0
    queue.append((i, j, depth))

    while queue:
        i, j, depth = queue.popleft()
        if i == goal[0] and j == goal[1]:
            print(depth)
            break
        for direction in range(8):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if 0 <= check_i < board_size and 0 <= check_j < board_size and not visited[check_i][check_j]:
                visited[check_i][check_j] = True
                queue.append((check_i, check_j, depth + 1))


for test_case in range(1, int(input()) + 1):
    board_size = int(input())
    start = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    visited = [[False] * board_size for _ in range(board_size)]
    bfs(start[0], start[1])