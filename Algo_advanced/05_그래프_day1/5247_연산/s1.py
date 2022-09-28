# 5247_연산

from collections import deque
import sys
sys.stdin = open('input.txt')

calculator_idx = [1, 2, 3, 4]


def bfs_calculate(num):
    global count
    global result

    queue = deque()
    count += 1

    for i in range(1, 5):
        queue.append((calculator[i], count))

    while queue:
        visited = [0] * 5
        for i in range(1, 5):
            if not visited[i]:
                visited[i] = 1
                cal_func = queue.popleft()[0]
                result = cal_func(num)
                print(result, count)
                queue.append((calculator[i], count + 1))

    # bfs_calculate(result)



calculator = {1: lambda x: x + 1, 2: lambda x: x - 1, 3: lambda x: x * 2, 4: lambda x: x - 10}


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    result = 0
    count = 0
    bfs_calculate(N)
    print()

