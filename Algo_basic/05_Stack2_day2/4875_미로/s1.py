# 4875_미로

import sys
sys.stdin = open("input.txt")

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# DFS 함수
def dfs(vx, vy):
    global result       # 미로를 찾으면 표시해줄 변수
    visited[vx][vy] = True  # 방문한 지점을 표시

    # 델타 검색
    for k in range(4):
        nx = vx + dx[k]     # 행 방향의 다음 좌표 설정
        ny = vy + dy[k]     # 열 방향의 다음 좌표 설정

        # 미로의 범위를 벗어나지 않고, 방문한 지점이 아니며, 미로가 막혀있지 않을 때('1'이 아닐 때)
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != '1':
            # DFS로 찾은 경로에 출구가 있다면
            if maze[nx][ny] == '3':
                result = 1  # 미로를 찾음
                break
            dfs(nx, ny)     # 새로운 지점에서의 DFS 수행


for test_case in range(1, int(input()) + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    start_i = 0
    start_j = 0
    
    # 반복문을 돌면서 시작지점('2'로 표시된 지점)을 찾음
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_i = i
                start_j = j
    
    stack = []      # 스택 초기화
    result = 0      # 일단 result를 0으로 초기화하여 DFS 함수의 if문에 걸리지 않는다면 기본적으로 0으로 출력됨
    visited = [[False] * N for _ in range(N)]   # 방문 리스트 초기화
    dfs(start_i, start_j)   # 입구에서 DFS를 수행

    print(f'#{test_case} {result}')