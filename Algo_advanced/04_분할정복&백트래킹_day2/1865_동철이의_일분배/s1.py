# 1865_동철이의 일분배

import sys
sys.stdin = open('input.txt')


def distribute_work(arr, start, end, j):
    global max_p
    global p

    arr_length = len(arr)
    if p <= max_p:
        return

    if start == end:
        if p > max_p:
            max_p = p
        return

    for i in range(arr_length):
        if used[i] == 0:
            used[i] = 1
            success_rate = success_rate_list[i][j]
            if success_rate == 0:
                success_rate = 1
            p *= success_rate * 0.01
            distribute_work(arr, start + 1, end, j + 1)
            p /= success_rate * 0.01
            used[i] = 0


for test_case in range(1, int(input()) + 1):
    N = int(input())
    success_rate_list = [list(map(int, input().split())) for _ in range(N)]
    a = [i for i in range(N)]

    used = [0] * N
    result = []
    pick = []
    p = 1
    max_p = 0
    distribute_work(a, 0, N, 0)

    print(f'#{test_case} {(max_p * 100):.6f}')
