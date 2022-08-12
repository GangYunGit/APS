# 9386_연속한_1의_개수. sol_2

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_row = input()

    count_1 = 0
    counter = [0] * N

    for i in range(N):
        if num_row[i] == '1':
            count_1 += 1
            counter[i] = count_1
        else:
            count_1 = 0
            counter[i] = count_1

    max = 0
    for j in counter:
        if j > max:
            max = j

    print(f'#{test_case} {max}')