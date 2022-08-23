# 5209_최소_생산_비용

import sys
sys.stdin = open("input.txt")


def permutations(i, sum_val):
    global min_val
    # 뽑고 싶은 만큼 뽑았다면 출력 및 종료
    if sum_val < min_val and i == N - 1:
        min_val = sum_val
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            sum_val += board[i][j]

            permutations(i + 1, sum_val)

            visited[j] = False

    print(min_val)
        # if sum_val < min_val:
        #     min_val = sum_val


for test_case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_val = 2000000000

    permutations(0, 0)
