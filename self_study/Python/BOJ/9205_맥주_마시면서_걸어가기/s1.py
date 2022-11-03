# BOJ_9205. 맥주 마시면서 걸어가기
from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()

        for next_i, next_j in GS24:
            if next_i == home[0] and next_j == home[1]:
                print(next_i, next_j)
                print("happy")
                break
            if abs(next_i - i) + abs(next_j - j) <= 1000:
                queue.append((next_i, next_j))
    else:
        print("sad")


for test_case in range(1, int(input()) + 1):
    GS24_num = int(input())
    home = tuple(map(int, input().split()))
    GS24 = {tuple(map(int, input().split())) for _ in range(GS24_num)}
    goal = tuple(map(int, input().split()))
    GS24.add(home)
    GS24.add(goal)
    # visited = [False for _ in range(GS24_num)]
    # bfs(goal[0], goal[1])
    print(GS24)





