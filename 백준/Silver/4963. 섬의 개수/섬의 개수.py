import sys
sys.setrecursionlimit(100000)

# 상 우상 우 우하 하 좌하 좌 좌상 (시계방향)
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


# DFS 탐색 함수
def dfs(x, y):
    visited[x][y] = True    # 방문한 좌표를 표시

    # 델타 검색
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        # 지정한 델타 방향의 정점이 지도의 범위 내에 있고, 방문하지 않았고, land인 경우
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and map_info[nx][ny] == 1:
            dfs(nx, ny)     # 다음 방향의 델타 검색을 수행


while True:
    w, h = map(int, input().split())    # 열, 행

    # w, h에 모두 0이 들어오면 테스트 케이스를 종료
    if w == 0 and h == 0:
        break

    # 지도의 좌표 초기화, 방문 리스트 초기화,
    map_info = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    island_count = 0

    # 행 우선 순회
    for i in range(h):
        for j in range(w):
            # 방문하지 않았고, land 를 만나면 dfs 수행
            if not visited[i][j] and map_info[i][j] == 1:
                dfs(i, j)
                island_count += 1    # dfs 수행이 완료되면 섬으로 판정

    print(island_count)