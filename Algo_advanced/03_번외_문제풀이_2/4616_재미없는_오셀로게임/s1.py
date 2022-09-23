# 4616_재미있는 오셀로 게임

import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 상 우 하 좌 우상 우하 좌하 좌상
di = [-1, 0, 1, 0, 1, -1, -1, 1]
dj = [0, 1, 0, -1, 1, 1, -1, -1]

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    stone_info = [list(map(int, input().split())) for _ in range(M)]
    white_count = 0
    black_count = 0
    # print(stone_info)

    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    # print(board)

    for stone in stone_info:
        if stone[2] == 1:
            put_i = stone[1] - 1
            put_j = stone[0] - 1
            board[put_i][put_j] = 1
            # 흑돌 선공
            for k in range(8):
                for circle in range(1, N):
                    n_i = put_i + di[k] * circle
                    n_j = put_j + dj[k] * circle
                    if 0 <= n_i < N and 0 <= n_j < N and board[n_i][n_j] == 1:
                        for plus in range(1, circle):
                            board[put_i + di[k] * plus][put_j + dj[k] * plus] = 1
                        break

        else:
            put_i = stone[1] - 1
            put_j = stone[0] - 1
            board[put_i][put_j] = 2
            # 백돌 후공
            for k in range(8):
                for circle in range(1, N):
                    n_i = put_i + di[k] * circle
                    n_j = put_j + dj[k] * circle
                    if 0 <= n_i < N and 0 <= n_j < N and board[n_i][n_j] == 2:
                        for plus in range(1, circle):
                            board[put_i + di[k] * plus][put_j + dj[k] * plus] = 2
                        break

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black_count += 1
            elif board[i][j] == 2:
                white_count += 1

    print(f'#{test_case} {black_count} {white_count}')