# 6190_정곤이의 단조 증가하는 수

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num = 0
    growing = []

    for a_j in range(N - 1, -1, -1):

        for a_i in range(a_j):
            num = num_list[a_i] * num_list[a_j]
            check = 0
            for idx in range(len(str(num)) - 1):
                if str(num)[idx] > str(num)[idx + 1]:
                    break
                else:
                    check += 1
            if check == len(str(num)) - 1:
                growing.append(num)

    if not growing:
        result = -1
    else:
        result = max(growing)

    print(f'#{test_case} {result}')