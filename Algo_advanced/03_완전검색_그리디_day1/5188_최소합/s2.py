# 5188_최소합 (DP로 풀기)
import sys
sys.stdin = open('input.txt', encoding='utf-8')

for test_case in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    memo = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 1. 원래 리스트의 값을 더한다
            memo[i][j] = matrix[i][j]

            if i == 0 and j == 0:
                continue

            # 2. 위와 왼쪽을 더해서 최소합으로 갱신
            if i == 0:
                memo[i][j] += memo[i][j - 1]
            elif j == 0:
                memo[i][j] += memo[i - 1][j]
            else:
                memo[i][j] += min(memo[i][j - 1], memo[i - 1][j])

    print(f'#{test_case} {memo[N - 1][N - 1]}')
    