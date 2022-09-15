# 5097_회전
from collections import deque

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    N, shift = map(int, input().split())            # 수열의 크기N, 움직일 횟수 shift 입력
    num_list = deque((map(int, input().split())))   # 수열을 deque에 입력하여 담음

    # M번 만큼 숫자를 뒤로 보내는 작업을 진행
    for _ in range(shift):
        num_list.append(num_list.popleft())

    print(f'#{test_case} {num_list[0]}')
