# 1954_달팽이_숫자

import sys
sys.stdin = open("input.txt")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for test_case in range(1, T):
    N = int(input())
    snail = [[0] * N for _ in range(N)]  # 이차원 리스트 초기화 국룰

    x, y = 0, 0  # 처음 출발 위치
    direction = 0  # 처음 출발 방향은 오른쪽

    for i in range(1, N * N + 1):
        snail[x][y] = i     # 출력해줄 값
        # 다음 위치 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위안에 있고, 숫자가 없는가?
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            x, y = nx, ny
        else:
            # 방향을 바꿔서 다시 이동하자
            direction = (direction + 1) % 4  # 인덱스가 3을 넘어가게 되면 다시 0부터 시작
            x += dx[direction]
            y += dy[direction]

    print(f'#{test_case} ')
    for line in snail:
        print(*line)