# 5204_병합정렬
from collections import deque
import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    # global count

    arr_length = len(arr)
    if arr_length == 1:
        return arr

    left = deque()
    right = deque()
    for i in range(0, arr_length // 2):
        left.append(arr[i])

    for i in range(arr_length // 2, arr_length):
        right.append(arr[i])

    left = deque(merge_sort(left))
    right = deque(merge_sort(right))

    # if left[-1] > right[-1]:
    #     count += 1

    return merge(left, right)


def merge(left, right):
    global count
    result = []

    if left[-1] > right[-1]:
        count += 1

    print(left, right)
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif len(left) > 0:
            result.append(left.popleft())
        elif len(right) > 0:
            result.append(right.popleft())

    return result


for test_case in range(1, int(input()) + 1):
    N = int(input())
    unsorted_list = list(map(int, input().split()))
    count = 0
    sorted_list = merge_sort(unsorted_list)
    print(f'#{test_case} {sorted_list[N // 2]} {count}')
