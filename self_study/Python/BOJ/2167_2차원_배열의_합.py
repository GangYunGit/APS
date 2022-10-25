# BOJ_2167. 2차원 배열의 합

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(N)]


K = int(input())
for _ in range(K):
    result = 0
    i, j, x, y = map(int, input().split())
    total = sum(sum(num_list[i]) for i in range(N))
    nums = (x - i + 1) * (y - j + 1)
    if nums < N * M // 2:
        for row in range(i - 1, x):
            for col in range(j - 1, y):
                result += num_list[row][col]
    else:
        for row in range(0, i - 1):
            for col_1 in range(0, j - 1):
                total -= num_list[row][col_1]
            for col_2 in range(y, M):
                total -= num_list[row][col_2]

        for row in range(i - 1, x):
            for col_1 in range(0, j - 1):
                total -= num_list[row][col_1]
            for col_2 in range(y, M):
                total -= num_list[row][col_2]
        result = total

    print(result)
