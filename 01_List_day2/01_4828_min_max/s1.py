# 4828_min_max

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    a_i = list(map(int,input().split()))
    max_val = 0
    min_val = 1000000

    for num in a_i:
        if num > max:
            max = num
        if num < min:
            min = num

    print(f'#{test_case} {max-min}')
