from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j, n, m, maps):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((i, j, 1))
    
    while queue:
        pi, pj, depth = queue.popleft()
        if (pi, pj) == (n - 1, m - 1):
            return depth
        for direction in range(4):
            check_i = pi + di[direction]
            check_j = pj + dj[direction]
            if 0 <= check_i < n and 0 <= check_j < m and not visited[check_i][check_j] and maps[check_i][check_j] != 0:
                visited[check_i][check_j] = True
                queue.append((check_i, check_j, depth + 1))
    
    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs(0, 0, n, m, maps)
    return answer