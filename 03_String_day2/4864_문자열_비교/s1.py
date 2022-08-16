# 4864_문자열_비교

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    str_1 = input()
    str_2 = input()
    result = 0

    # str2에서 str1와 같은 문자열이 포함되어있는지 확인
    if str_2.count(str_1) == 1:
        result = 1

    print(f'#{test_case} {result}')
