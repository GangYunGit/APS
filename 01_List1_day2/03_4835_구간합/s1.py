# 4835_구간합
# 슬라이딩 윈도우 방식으로 한번 풀어보자!

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a_i = list(map(int, input().split()))   # 정수 a_i가 담긴 리스트
    min = 2000000000    # min 비교값을 매우 크게 초기화(최대 100개의 구간 * 최대값 10000 보다 크게)
    max = 0     # 양수이므로 max 비교값을 0으로 초기화
    filter = 0      # 결과 출력값

    for i in range(N - M + 1):  # N의 구간에서 M만큼의 길이에 대한 경우의 수
        n_sum = 0   # 각 구간마다의 합
        for j in range(M):  # 각 구간의 합을 구하는 반복문
            n_sum += a_i[i + j] # i 번쨰 , i + 1번째 , ..., i + M-1 번째 까지의 합
        if n_sum > max:    # 최대값
            max = n_sum
        if n_sum < min:    # 최소값
            min = n_sum

    filter = max - min
    print(f'#{test_case} {filter}')

