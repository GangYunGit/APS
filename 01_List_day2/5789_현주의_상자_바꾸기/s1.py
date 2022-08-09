# 5789_현주의_상자_바꾸기

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    box_list = [0] * N

    for i in range(1, Q + 1):   # Q크기 만큼의 입력을 받기 위한 반복문
        L, R = map(int, input().split())
        for change in range(L - 1, R):  # index상으로는 L - 1번째이지만 실제로는 L번째
            box_list[change] = i    # 선택된 L~R영역의 값을 i로 바꿈

    print(f'#{test_case}', end=' ')
    print(*box_list)    # unpaking을 통해 리스트의 값을 형식에 맞추어 출력

