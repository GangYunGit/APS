# 2001_파리퇴치

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            flies_sum = 0
            for row in range(M):
                for col in range(M):
                    flies_sum += board[i + row][j + col]
            if flies_sum >= max_flies:
                max_flies = flies_sum

    print(f'#{test_case} {max_flies}')
