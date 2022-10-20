# BOJ_6603. 로또

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def dfs(numbers, nums, start):

    if len(pick) == 6:
        print(*pick)
        return

    for i in range(start, nums):
        if not pick or numbers[i] > max(pick):
            if not used[i]:
                used[i] = True
                pick.append(numbers[i])
                dfs(numbers, nums, start + 1)
                pick.pop()
                used[i] = False


while True:
    num_list = list(map(int, input().split()))
    if num_list == [0]:
        break
    pick = []
    used = [False for _ in range(num_list[0])]
    dfs(num_list[1:], num_list[0], 0)
    print()
