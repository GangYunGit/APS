# 5208_전기버스2

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def move(start, end, battery, charge):
    global min_val          # 백트래킹에 사용할 충전의 최소값

    if charge >= min_val:   # 충전 횟수가 이전에 계산된 최소값 이상이면 함수 종료
        return

    if start >= end:        # 버스가 종점에 도달해도 함수 종료
        return

    # 도달한 정류장에서 충전가능한 배터리 용량으로 갈 수 있는 경우의 수
    for i in range(1, charger[start] + 1):

        # 아직 종점에 도달하지 못하였다면
        if start + i < end:
            # 일단 충전을 한 후 모든 경우의 수를 다시 탐색
            move(start + i, end, battery - i, charge + 1)

        # 종점에 도달했다면
        else:
            # 최소값이라면 최신화 후 함수호출 해제
            if charge < min_val:
                min_val = charge
            return


for test_case in range(1, int(input()) + 1):
    bus_info = list(map(int, input().split()))
    bus_num = bus_info[0]
    bus_stop = [_ for _ in range(1, bus_num + 1)]
    charger = bus_info[1:] + [0]
    min_val = 101

    move(0, bus_num - 1, charger[0], 0)
    print(f'#{test_case} {min_val}')

