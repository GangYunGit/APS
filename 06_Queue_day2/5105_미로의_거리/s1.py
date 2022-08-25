# 5105_미로의_거리

import sys
sys.stdin = open("input.txt")

# 좌 상 우 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


# BFS 함수 구현
def bfs(x, y):
    visited[x][y] = 1       # 방문 표시
    queue.append((x, y))    # 방문한 곳을 큐에 enQueue
    
    # 큐가 빌 때까지 실행
    while queue:
        x, y = queue.pop(0)     # deQueue
        # 4방향 델타 검색 실행
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 범위를 벗어나지 않고, 방문하지 않았으며, 미로가 벽이 아닌 곳
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and maze[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1     # 다음 지점으로 갈 때마다 방문 값을 1씩 더해줌
                queue.append((nx, ny))                  # 인접 지점을 enQueue
                # 출구를 만나면 거리를 계산하고 함수 종료
                if maze[nx][ny] == 3:                   
                    return visited[x][y] - 1    
    
    return 0    # 출구를 찾지 못하면 0을 반환하고 종료


for test_case in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    queue = []
    count = 0

    # 시작지점을 찾기위한 반복문
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j

    print(f'#{test_case} {bfs(start_i, start_j)}')