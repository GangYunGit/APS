# BOJ_5014. 스타트링크
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, count):

    visited[start] = True
    count += 1
    queue = deque()

    if start == goal:
        print(0)
        return

    queue.append(((start + up, start - down), count))

    while queue:
        next_floors = queue.popleft()
        count = next_floors[1]
        # print(next_floors)
        for next_floor in next_floors[0]:
            if 0 < next_floor <= top_floor and not visited[next_floor]:
                visited[next_floor] = True
                if next_floor < goal:
                    queue.append(((next_floor + up, next_floor - down), count + 1))
                elif next_floor > goal:
                    queue.append(((next_floor + up, next_floor - down), count + 1))
                else:
                    print(count)
                    break

    if not visited[goal]:
        print("use the stairs")


top_floor, now, goal, up, down = map(int, input().split())
visited = [False for _ in range(top_floor + 1)]
# print(visited)
bfs(start=now, count=0)


