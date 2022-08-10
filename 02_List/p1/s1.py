# 델타 검색

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    grid = [list(map(int,input().split())) for i in range(N)]
    grid_sum = 0

    di = [0, 0, -1, 1]  # 상 하
    dj = [-1, 1, 0, 0]  # 좌 우
    for i in range(N):  # i의 오른쪽 방향으로 탐색
        for j in range(N):  # j의 오른쪽 방향으로 탐색
            for k in range(4):
                n_i = i + di[k] # (i, j)의 상하 방향 => (i - 1, j), (i + 1, j)
                n_j = j + dj[k] # (i, j)의 좌우 방향 => (i, j - 1), (i, j + 1)
                # 범위를 넘어서는 경우 예외처리
                if 0 <= n_i <= (N - 1) and 0 <= n_j <= (N - 1):
                    # grid_sum 변수에 차의 절댓값의 합을 모두 더함
                    grid_sum += abs(grid[i][j] - grid[n_i][n_j])

    print(f'#{test_case} {grid_sum}')



