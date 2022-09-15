# 1225_암호생성기

import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    queue = list(map(int, input().split()))

    # queue의 마지막 숫자가 0이면 반복문을 탈출
    while queue[7] != 0:

        # 1~5까지 증가시키며 deQueue값에서 빼줌
        for i in range(1, 6):
            shift = queue.pop(0)      # deQueue값 저장
            queue.append(shift - i)   # deQueue에서 i를 뺀후 enQueue

            # queue의 마지막 숫자가 0보다 작거나 같아지면 0으로 바꾸고 탈출
            if queue[7] <= 0:
                queue[7] = 0
                break

    print(f'#{test_case}', end=' ')
    print(*queue)

