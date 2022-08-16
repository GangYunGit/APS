# 9368_점점_커지는_당근의_개수

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dangun = input().split()
    count = 0
    count_list = [0] * N

    for i in range(N - 1):
        if int(dangun[i + 1]) - int(dangun[i]) == 1:
            count += 1
            count_list[i] = count
        else:
            count = 0
            count_list[i] = count

    print(f'#{test_case} {max(count_list) + 1}')

