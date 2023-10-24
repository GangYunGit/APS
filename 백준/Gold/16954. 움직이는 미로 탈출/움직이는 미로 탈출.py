from collections import deque

di = [0, -1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, 0, -1, 1, -1, 1, -1, 1]


def bfs(i, j):
    visited = [[False] * 8 for _ in range(8)]
    queue = deque([(i, j)])

    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            visited[i][j] = False
            if maze[i][j] == '#':
                continue
            if i == 0:
                return 1
            for direction in range(9):
                check_i, check_j = i + di[direction], j + dj[direction]
                if 0 <= check_i < 8 and 0 <= check_j < 8 and not visited[check_i][check_j] and maze[check_i][check_j] == '.':
                    visited[check_i][check_j] = True
                    queue.append((check_i, check_j))

        maze.pop()
        maze.insert(0, ['.' for _ in range(8)])

    return 0


maze = [list(input().rstrip()) for _ in range(8)]

print(bfs(7, 0))