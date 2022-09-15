# 2005_파스칼의_삼각형

import sys

sys.stdin = open('input.txt')


for test_case in range(1, int(input()) + 1):
    N = int(input())
    row = []

    print(f'#{test_case}')
    for i in range(N):

        # 첫번째 삼각형은 [1], 두번째 삼각형은 [[1],[1,1]]로 시작
        if i < 2:
            row.append(1)

        # 세번째 삼각형을 예로 들면
        # 1 2 1 => 1 (1+2) (2+1) 로 변경 후
        # .append(1)을 하여 1 3 3 1로 변경
        else:
            row.append(1)
            for j in range(1, i):
                row[i - j] = row[i - j - 1] + row[i - j]
        print(*row)     # 변경된 값을 출력