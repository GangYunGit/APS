import sys
from itertools import product
sys.stdin = open('input.txt')

for test_case in range(1, int(input()) + 1):
    N = int(input())
    calculator_info = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_num = -100000000
    min_num = 100000000

    calculator_list = ['+', '-', '*', '/']

    for calculators in product(calculator_list, repeat=N - 1):

         if calculators.count('+') == calculator_info[0] and calculators.count('-') == calculator_info[1] and calculators.count('*') == calculator_info[2]:
             print(calculators)
    #         new_num = num_list[0]
    #         for i in range(N - 1):
    #             if calculators[i] == '+':
    #                 new_num += num_list[i + 1]
    #             elif calculators[i] == '-':
    #                 new_num -= num_list[i + 1]
    #             elif calculators[i] == '*':
    #                 new_num *= num_list[i + 1]
    #             else:
    #                 new_num //= num_list[i + 1]
    #
    #         if new_num > max_num:
    #             max_num = new_num
    #         if new_num < min_num:
    #             min_num = new_num
    #
    #
    # print(f'#{test_case} {max_num - min_num}')
