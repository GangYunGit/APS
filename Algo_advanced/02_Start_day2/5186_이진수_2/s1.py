# 5186_이진수2

import sys
sys.stdin = open('input.txt', encoding='utf-8')

for test_case in range(1, int(input()) + 1):
    bin_num = float(input())
    result = ''

    i = 0
    while bin_num != 0:
        i += 1
        if bin_num - (2 ** -i) >= 0:
            result += '1'
            bin_num -= (2 ** -i)
        else:
            result += '0'

        if len(result) >= 13:
            result = 'overflow'
            break

    print(f'#{test_case} {result}')


