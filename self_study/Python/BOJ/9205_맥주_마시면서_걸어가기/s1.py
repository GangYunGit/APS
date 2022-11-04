# BOJ_9205. 맥주 마시면서 걸어가기
from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        temp_i, temp_j = queue.popleft()
        if {key, (temp_i, temp_j)} in GS24.items():
            if abs(temp_i - i) + abs(temp_j - j) <= 1000:
                queue.append((temp_i, temp_j))
    else:
        print("sad")


for test_case in range(1, int(input()) + 1):
    GS24_num = int(input())
    home = tuple(map(int, input().split()))
    GS24 = {i: tuple(map(int, input().split())) for i in range(GS24_num)}
    goal = tuple(map(int, input().split()))

    visited = [False for _ in range(GS24_num + 1)]
    # bfs(goal[0], goal[1])
    print(GS24)
    for (temp_i, temp_j) in GS24.values():
        print(temp_i, temp_j)





