# 13702_델타검색

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for test_case in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    sum_abs = 0
    sum_board = 0
    for x in range(N):
        for y in range(N):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    sum_abs += abs(board[nx][ny] - board[x][y])
    sum_board += sum_abs

    print(f'#{test_case} {sum_board}')