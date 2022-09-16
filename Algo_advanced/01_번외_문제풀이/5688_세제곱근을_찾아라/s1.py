# 5688_세제곱근을_찾아라

import sys
sys.stdin = open('input.txt', encoding='utf-8')


for test_case in range(1, int(input()) + 1):
    N = int(input())
    result = -1

    # N이 0부터 10^18까지이므로 i를 10^6까지 반복시키면서 확인하면 된다.
    for i in range(1, 1000001):
        if i ** 3 == N:
            result = i
            break

    print(f'#{test_case} {result}')
