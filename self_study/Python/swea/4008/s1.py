import sys
from itertools import permutations
sys.stdin = open('input.txt')

for test_case in range(1, int(input()) + 1):
    N = int(input())
    calculator_info = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_num = -100000000
    min_num = 100000000

    calculator_list = []
    for i in range(len(calculator_info)):
        if i == 0:
            for _ in range(calculator_info[i]):
                calculator_list.append('+')
        elif i == 1:
            for _ in range(calculator_info[i]):
                calculator_list.append('-')
        elif i == 2:
            for _ in range(calculator_info[i]):
                calculator_list.append('*')
        else:
            for _ in range(calculator_info[i]):
                calculator_list.append('/')
    for i in list(permutations(calculator_list, N - 1)):
        print(i)

