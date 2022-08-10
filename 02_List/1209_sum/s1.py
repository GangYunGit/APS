# 1209_Sum
import sys
sys.stdin = open("input.txt")

for test_case in range(1, 11):
    T = int(input())
    list_num = [list(map(int, input().split())) for i in range(100)]
    right_down_sum = 0
    left_down_sum = 0
    max_sum = 0

    for i in range(100):
        row_sum = 0
        col_sum = 0

        right_down_sum += list_num[i][i]    # 오른쪽 아래 대각선 방향의 합
        if right_down_sum > max_sum:
            max_sum = right_down_sum    # max값과 비교

        left_down_sum += list_num[i][99-i]  # 왼쪽 아래 대각선 방향의 합
        if left_down_sum > max_sum:
            max_sum = left_down_sum     # max값과 비교

        for j in range(100):
            row_sum += list_num[i][j]   # 행방향의 합 x 100개
            col_sum += list_num[j][i]   # 열방향의 합 x 100개

        if row_sum > max_sum:   # 행방향의 합을 구할 때마다 max값과 비교
            max_sum = row_sum
        if col_sum > max_sum:   # 열방향의 합을 구할 때마다 max값과 비교
            max_sum = col_sum

    print(f'#{T} {max_sum}')