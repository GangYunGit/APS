# 5201_컨테이너_운반

import sys
sys.stdin = open('input.txt', encoding='utf-8')

for test_case in range(1, int(input()) + 1):
    container_num, truck_num = map(int, input().split())
    container_weight = list(map(int, input().split()))
    truck_capacity = list(map(int, input().split()))

    container_weight.sort()
    truck_capacity.sort()

    result = 0

    for i in range(container_num - 1, -1, -1):
        if truck_capacity and container_weight[i] <= truck_capacity[-1]:
            truck_capacity.pop()
            result += container_weight[i]
            if not truck_capacity:
                break

    print(f'#{test_case} {result}')
