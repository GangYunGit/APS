# 부분집합 합

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(T):
    list_a = list(map(int,input().split()))

    for i in range(1<<10):
        if i == 0:  # 공집합의 원소의 합이 0으로 계산되는 것을 제외
            continue
        sum_part = 0    # 각 부분집합의 합을 할당할 변수
        for j in range(10):
            if i & (1<<j):
                sum_part += list_a[j]   # 부분집합의 모든 원소의 합을 구함
        if sum_part == 0:   # 부분집합의 합이 0일 때 반복문 탈출 후 1을 출력
            result = 1
            break
        else:
            result = 0  # 부분집합의 합이 0이 아니라면 0을 출력
    print(f'#{test_case} {result}')



