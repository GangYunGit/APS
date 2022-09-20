# 5185_이진수
import sys
sys.stdin = open('input.txt', encoding='utf-8')

for test_case in range(1, int(input()) + 1):
    N, hex_num = input().split()
    N = int(N)
    result = ''

    bin_nums_list = [bin(int(hex_num[i:i + 1:], 16))[2::] for i in range(N)]
    for bin_num in bin_nums_list:
        while len(bin_num) != 4:
            bin_num = '0' + bin_num
        result += bin_num

    print(f'#{test_case} {result}')
