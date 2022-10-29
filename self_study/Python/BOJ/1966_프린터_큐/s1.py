# BOJ_1966 프린터 큐
from collections import deque

for test_case in range(1, int(input()) + 1):
    N, now_queue = map(int, input().split())
    priority = deque(map(int, input().split()))
    idx = deque([_ for _ in range(N)])
    count = 0

    while priority:
        if priority[0] == max(priority):
            printed = idx.popleft()
            priority.popleft()
            count += 1
            # print(idx)
            if printed == now_queue:
                break

        else:
            idx.rotate(-1)
            priority.rotate(-1)
            # print(idx)

    print(count)