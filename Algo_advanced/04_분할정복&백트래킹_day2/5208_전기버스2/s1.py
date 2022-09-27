# 5208_전기버스2

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def move(start, battery, count):
    if start >= end:
        return count

    return move(start + 1, battery - 1, count + 1)


for test_case in range(1, int(input()) + 1):
    bus_info = list(map(int, input().split()))
    bus_num = bus_info[0]
    bus_stop = [_ for _ in range(1, bus_num + 1)]
    charger = bus_info[1:] + [0]
    print(bus_stop)
    print(charger)

    start = 0
    count = 0
    end = bus_num - 1
    print(move(start, charger[start], 0))

