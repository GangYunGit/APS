# BOJ_9205. 맥주 마시면서 걸어가기
from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        temp_i, temp_j = queue.popleft()
        if temp_i == home[0] and temp_j == home[1]:
            print("happy")
            break

        for key, points in GS24.items():
            distance = abs(points[0] - temp_i) + abs(points[1] - temp_j)
            if not visited[key] and distance <= 1000:
                visited[key] = True
                queue.append((points[0], points[1]))

    else:
        print("sad")


for test_case in range(1, int(input()) + 1):
    GS24_num = int(input())
    home = tuple(map(int, input().split()))
    GS24 = {i: tuple(map(int, input().split())) for i in range(GS24_num)}
    GS24[GS24_num] = home
    goal = tuple(map(int, input().split()))

    visited = [False for _ in range(GS24_num + 1)]
    bfs(goal[0], goal[1])


