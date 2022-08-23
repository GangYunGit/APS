# 4881_배열_최소_합

# 순열 내장함수 import
from itertools import permutations

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_val = 10 * N * N    # 최소값 비교할 변수 지정
    idx_list = [i for i in range(N)]
    cnt = 0

    # 2차원 리스트의 행 인덱스를 0 ~ N까지 순열의 경우의 수로 지정
    for line in permutations(idx_list, N):
        sum_val = 0

        # 열 인덱스는 0 ~ N까지 순차적으로 증가
        for k in range(N):
            sum_val += board[line[k]][k]    # 선택된 구간의 합을 구함
            cnt += 1
            if sum_val > min_val:   # 백트래킹 : 합을 구하는 도중에 이전에 저장된 최소값을 넘어서는 경우 break
                break

        # 구간의 합이 구해질 때 마다 최소값을 최신화
        if sum_val < min_val:
            min_val = sum_val

    print(f'#{test_case} {min_val}')
    print(cnt)
