# 4843_특별한_정렬

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    special_list = [0] * 10

    for i in range(N - 1, 0, -2): # 9, 7, 5, 3, 1
        for j in range(i):  # 9, 7, 5, 3, 1
            if num_list[j] >= num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
        for j in range(i - 1):  # 8, 6, 4, 2, 0
            if num_list[j] <= num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    for k in range(0, 10):
        special_list[k] = num_list[N - k - 1]

    print(f'#{test_case}', end=' ')
    print(*special_list)

