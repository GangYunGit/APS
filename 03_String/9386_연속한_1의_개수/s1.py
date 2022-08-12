# 9386_연속한_1의_개수. sol_1

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    row = input()
    count = 0
    count_list = []

    for num in row:
        if num == '1':
            count += 1
            count_list.append(count)
        else:
            count = 0
            count_list.append(count)

    print(f'#{test_case} {max(count_list)}')