# 1289_원재의 메모리 복구하기

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    memory = input()
    count = 0

    for i in range(len(memory) - 1, 0, -1):
        if memory[i] != memory[i - 1]:
            count += 1

    if memory[0] == '1':
        count += 1

    print(f'#{test_case} {count}')

