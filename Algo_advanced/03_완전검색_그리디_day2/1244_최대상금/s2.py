# 1244_최대상금

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def dfs(nums_list, start):

    if start == int(change):
        nums_comb.append(list(nums_list))
        return

    for i in range(start, int(change)):
        nums_list[start], nums_list[i] = nums_list[i], nums_list[start]
        dfs(nums_list, start + 1)
        nums_list[start], nums_list[i] = nums_list[i], nums_list[start]


for test_case in range(1, int(input()) + 1):
    nums, change = input().split()
    num_list = ' '.join(nums).split()
    for i in range(len(nums)):
        num_list[i] = int(num_list[i])

    nums_comb = []
    max_num = 0
    dfs(num_list, 0)
    print(nums_comb)
    for nums in nums_comb:
        result = 0
        length = len(nums)
        for i in range(length):
            result += nums[i] * 10 ** (length - i - 1)
        if result > max_num:
            max_num = result
        print(max_num)


