from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j, n, m, maps):
    visited = [[False] * m for _ in range(n)]   # 방문한 지점을 저장하기 위한 2차원 배열 생성
    queue = deque()
    depth = 1
    queue.append((i, j, depth))                 # 시작 지점과 bfs의 깊이(수행 횟수)를 tuple의 형태로 queue에 push
    
    while queue:                                
        pi, pj, depth = queue.popleft()
        if (pi, pj) == (n - 1, m - 1):
            return depth
        for direction in range(4):
            check_i = pi + di[direction]
            check_j = pj + dj[direction]
            # 확인할 부분이 게임판의 범위 내에 있고, 방문하지 않았고, 벽이 아닌경우에 방문처리
            if 0 <= check_i < n and 0 <= check_j < m and not visited[check_i][check_j] and maps[check_i][check_j] != 0:
                visited[check_i][check_j] = True
                queue.append((check_i, check_j, depth + 1))     # 다음 수행을 위해 queue에 방문지점을 push
    
    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs(0, 0, n, m, maps)
    return answer