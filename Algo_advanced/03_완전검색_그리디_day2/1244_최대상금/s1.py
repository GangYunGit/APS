# 1244_최대상금

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def selection_sort(arr, n, start):
    global count

    if count == n or start == len(arr) - 1:
        return

    max_idx = start
    for i in range(start, len(arr)):
        if arr[i] >= arr[max_idx]:
            max_idx = i

    if arr[start] < arr[max_idx]:
        arr[start], arr[max_idx] = arr[max_idx], arr[start]
        count += 1
        selection_sort(arr, n, start + 1)
    else:
        selection_sort(arr, n, start + 1)


for test_case in range(1, int(input()) + 1):
    nums, change = input().split()
    num_list = ' '.join(nums).split()
    for i in range(len(nums)):
        num_list[i] = int(num_list[i])

    count = 0
    selection_sort(num_list, int(change), 0)
    print(num_list, change)

