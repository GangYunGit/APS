# 5207_이진탐색

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def bin_search(arr, left, right, key, continuous):
    global count

    if left > right:
        return

    else:
        middle = (left + right) // 2
        if key == arr[middle]:
            if abs(continuous) < 2:
                count += 1
            return middle
        elif key < arr[middle]:
            if continuous == 1:
                return
            else:
                return bin_search(arr, left, middle - 1, key, 1)
        else:
            if continuous == -1:
                return
            else:
                return bin_search(arr, middle + 1, right, key, -1)


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    list_a = sorted(list(map(int, input().split())))
    list_b = sorted(list(map(int, input().split())))
    count = 0

    for i in range(M):
        visited = []
        num_b = list_b[i]
        bin_search(list_a, 0, N - 1, num_b, 0)

    print(f'#{test_case} {count}')
