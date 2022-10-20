# BOJ_14888. 연산자 끼워넣기

import sys
input = sys.stdin.readline


def dfs(calculator_info, idx_list):
    global max_num
    global min_num
    global cal_result
    if sum(calculator_info) == 0:
        cal_result = num_list[0]
        for i in range(num_length - 1):
            cal_result = calculators[idx_list[i]](cal_result, num_list[i + 1])
        if cal_result > max_num:
            max_num = cal_result
        if cal_result < min_num:
            min_num = cal_result
        return

    for i in range(4):
        if calculator_info[i] > 0:
            calculator_info[i] -= 1
            dfs(calculator_info, idx_list + [i])
            calculator_info[i] += 1


num_length = int(input())
num_list = list(map(int, input().split()))
calculator_info = list(map(int, input().split()))
result = []
max_num = -10 ** 9
min_num = 10 ** 9

calculators = {
    0: lambda x1, x2: x1 + x2,
    1: lambda x1, x2: x1 - x2,
    2: lambda x1, x2: x1 * x2,
    3: lambda x1, x2: -(-x1 // x2) if x1 < 0 else x1 // x2
}

cal_result = num_list[0]
dfs(calculator_info, [])
print(max_num)
print(min_num)
