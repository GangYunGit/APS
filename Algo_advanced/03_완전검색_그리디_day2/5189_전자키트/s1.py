# 5189_전자카트

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def permutations(arr, start):

    n = len(arr)
    if start == n:
        route_combs.append([0] + list(arr) + [0])
        return

    for i in range(start, n):
        arr[start], arr[i] = arr[i], arr[start]
        permutations(arr, start + 1)
        arr[start], arr[i] = arr[i], arr[start]


for test_case in range(1, int(input()) + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    route = [_ for _ in range(N)][1:]
    route_combs = []

    permutations(route, 0)
    min_battery_consume = 100 * N * N

    for i in range(len(route_combs)):
        battery_consume = 0
        for j in range(N):
            battery_consume += room[route_combs[i][j]][route_combs[i][j + 1]]
            if battery_consume >= min_battery_consume:
                break

        if battery_consume < min_battery_consume:
            min_battery_consume = battery_consume
    print(f'#{test_case} {min_battery_consume}')
