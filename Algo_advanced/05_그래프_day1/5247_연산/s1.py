# 5247_연산

from collections import deque
import sys
sys.stdin = open('input.txt')

calculator = {1: lambda x: x + 1, 2: lambda x: x - 1, 3: lambda x: x * 2, 4: lambda x: x - 10}


def bfs_calculate(num, count):
    queue = deque()
    count += 1
    queue.append((num, count))
    visited = [0] * 1000001
    visited[num] = 1

    while queue:
        num, count = queue.popleft()

        for i in range(1, 5):
            calculation_result = calculator[i](num)

            if calculation_result == M:
                return count

            if 0 < calculation_result <= 1000000 and not visited[calculation_result]:
                visited[calculation_result] = 1
                queue.append((calculation_result, count + 1))


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    print(f'#{test_case} {bfs_calculate(N, 0)}')
