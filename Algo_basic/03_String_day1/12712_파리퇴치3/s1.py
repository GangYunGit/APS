# 12712_파리퇴치3

import sys
sys.stdin = open("input.txt")

T = int(input())


# 델타 검색으로 스프레이의 분사 범위를 탐색
def search_flies(del_x, del_y, N, M, grid):
    sum_fly_list = []
    for i in range(N):
        for j in range(N):
            sum_fly = 0
            for k in range(1, M):   # M의 크기만큼 퍼져나감
                for direction in range(4):  # 4방향으로 퍼져나감
                    nx = i + del_x[direction] * k   # x방향의 탐색값
                    ny = j + del_y[direction] * k   # y방향의 탐색값
                    if 0 <= nx < N and 0 <= ny < N:
                        sum_fly += grid[nx][ny] # 한 칸에서 잡을 수 있는 파리의 마리 수
            sum_fly += grid[i][j]   # 정 가운데 칸의 파리의 마리 수
            sum_fly_list.append(sum_fly)    # 분사 범위 전체의 파리의 마리 수

    return max(sum_fly_list)    # 최대값 반환


dx = [-1, 1, 0, 0]  # 좌 우 -----
dy = [0, 0, -1, 1]  # ----- 상 하
dx_dia = [-1, -1, 1, 1]
dy_dia = [-1, 1, -1, 1]  # 좌상 좌하 우상 우하

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_fly = max(search_flies(dx, dy, N, M, grid), search_flies(dx_dia, dy_dia, N, M, grid))

    print(f'#{test_case} {max_fly}')



