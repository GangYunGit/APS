# 4831_전기버스

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    can_go, destination, charger_num = map(int, input().split())
    charger_list = list(map(int, input().split()))
    charger_row = [0] * (destination + can_go)  # index out of range error 방지
    my_location = 0
    charger_count = 0

    # charger_row에 충전소의 위치가 있는 곳을 1로 표시할 반복문
    # 종점이 10번 정류장이고 1, 3, 5, 7, 9에 충전소가 있다면 [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]로 표시됨
    for i in charger_list:
        charger_row[i] += 1
    # 이후 반복문에서 종점이 1로 표기되어있어야 지점을 찾아가기 때문에 종점에 충전소를 추가
    charger_row[destination] = 1

    while my_location < destination:    # 현재 위치를 계산한 값이 종점을 지나는 시점에서 반복 중지
        count = 0   # 충전소가 연속으로 없는 횟수를 카운트해주는 변수 초기화

        for j in range(can_go, 0, -1):
            # 현재 지점을 기준으로 가장 먼 곳의 충전소를 찾는 조건문
            if charger_row[my_location + j] == 1:
                my_location += j    # 이동한 만큼 나의 위치 증가
                charger_count += 1  # 충전 횟수
                break
            # 현재 지점에서 다음 충전소까지 충분한 거리가 나오지 않는다면 while문을 탈출
            else:
                count += 1
                # 최대 이동할 수 있는 정류장 수(can_go)와 같아지게 되면 다음 한칸을 이동할 수 없다.
                if count == can_go:
                    my_location += destination  # while문을 탈출해주기 위한 조건
                    charger_count = 1   # 결과를 0으로 맞추어주기 위한 값
                    break

    charger_count -= 1  # 종착역에 임의로 설치한 충전소 때문에 추가로 카운트된 1을 빼줌
    print(f'#{test_case} {charger_count}')










