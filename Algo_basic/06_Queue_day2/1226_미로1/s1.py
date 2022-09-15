# 1226_미로1

import sys
sys.stdin = open('input.txt')

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# BFS 함수 구현
def bfs(x, y):
    visited[x][y] = 1       # 방문 표시
    queue.append((x, y))    # enQueue

    # 큐가 비어있을 때까지
    while queue:
        x, y = queue.pop(0)     # deQueue

        # 4방향 델타 검색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 방문한 곳이 아니고, 가려는 방향이 벽이 아니면
            if visited[nx][ny] == 0 and maze[nx][ny] != 1:
                visited[nx][ny] = 1         # 방문 표시
                queue.append((nx, ny))      # 인접 정점 enQueue
                # 도착 지점을 찾았다면 1을 리턴
                if maze[nx][ny] == 3:
                    return 1

    # BFS 수행 완료 후에도 도착지점을 찾지 못했다면 0을 리턴
    return 0


for test_case in range(1, 11):
    # 입력
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 방문리스트, 큐 초기화
    visited = [[0] * 16 for _ in range(16)]
    queue = []

    print(f'#{test_case} {bfs(1, 1)}')
