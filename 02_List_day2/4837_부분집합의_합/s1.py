# 4837_부분집합의_합

import sys
sys.stdin = open("input.txt")

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
A = [i for i in range(1, 13)]

T = int(input())
for test_case in range(1, T + 1):   # 테스트 케이스
    N, K = map(int, input().split())    # N, K 입력
    count = 0   # 조건에 맞는 부분집합의 개수

    # --------부분집합을 구하는 반복문---------

    for i in range(1 << 12):
        sum_a = 0         # 부분집합의 합을 구해줄 변수(초기화 시점)
        subset_count = 0  # 부분집합의 원소의 개수를 구해줄 변수(초기화 시점)

        for j in range(12):
            if i & (1 << j):
                subset_count += 1   # 부분집합의 개수를 카운트
                sum_a += A[j]       # 부분집합의 합을 구함

    # ------부분집합을 구하는 반복문 종료------

        if subset_count == N and sum_a == K:    # 개수 == N, 합 == K일 때를 판별
            count += 1

    print(f'#{test_case} {count}')

