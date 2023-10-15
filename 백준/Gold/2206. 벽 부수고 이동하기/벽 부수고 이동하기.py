from collections import deque
import sys


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]      # 안 부순 visited, 부순 visited
    visited[i][j][0] = True
    queue = deque()
    queue.append((i, j, False, 1))     # 행 좌표, 열 좌표, 벽 부순 여부, 거리

    while queue:
        i, j, is_destroyed, distance = queue.popleft()
        if i == n - 1 and j == m - 1:
            return distance
        for direction in range(4):
            check_i, check_j = i + di[direction], j + dj[direction]
            if 0 <= check_i < n and 0 <= check_j < m:
                if board[check_i][check_j] == 1:
                    if not is_destroyed and not visited[check_i][check_j][1]:
                        visited[check_i][check_j][1] = True
                        queue.append((check_i, check_j, True, distance + 1))
                else:
                    if is_destroyed:
                        if not visited[check_i][check_j][1]:
                            visited[check_i][check_j][1] = True
                            queue.append((check_i, check_j, is_destroyed, distance + 1))
                    else:
                        if not visited[check_i][check_j][0]:
                            visited[check_i][check_j][0] = True
                            queue.append((check_i, check_j, is_destroyed, distance + 1))

    return -1


input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs(0, 0))