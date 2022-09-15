# 6485_삼성시의_버스노선

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    bus_stop = [0] * 5000   # 버스 정류장의 개수
    bus_loops = [[]] * N    # 배열의 index : 노선의 번호, 내부 배열의 값 : 노선번호가 Ai ~ Bi 정류장

    # 앞서 입력받은 노선의 개수N만큼 반복을 진행하면서 각 노선이 다니는 정류장 번호의 범위를 입력
    for i in range(N):
        bus_loops[i] = list(map(int,input().split()))

    P = int(input())    # 버스 정류장의 개수
    c_j = [0] * P       # 버스 정류장의 번호

    # 버스 정류장의 개수 = index, 번호 = value인 배열 생성(append함수와 동일)
    for p in range(P):
        c_j[p] = int(input())

    # 버스 노선의 범위를 1로 이루어진 띠로 생각하여, bus_stop배열에 카운팅하여 넣음
    for bus in bus_loops:
        for i in range(bus[0], bus[1] + 1):
            bus_stop[i] += 1

    # 결과를 출력할 배열 생성(append함수와 동일)
    result = [0] * P
    for j in range(P):
        result[j] = bus_stop[c_j[j]]

    print(f'#{test_case}', end=' ')
    print(*result)
