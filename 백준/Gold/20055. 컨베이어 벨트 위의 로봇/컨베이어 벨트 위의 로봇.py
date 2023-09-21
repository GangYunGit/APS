from collections import deque
import sys


def move_robot():
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    conveyor.rotate()

    # 내리는 위치는 일단 내려줌
    if conveyor[n - 1][1]:
        conveyor[n - 1][1] = False

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    check_robot = []
    for i in range(n - 2, -1, -1):
        if conveyor[i][1]:
            check_robot.append(i)

    for i in check_robot:
        if not conveyor[i + 1][1] and conveyor[i + 1][0] > 0:
            conveyor[i][1] = False
            conveyor[i + 1][1] = True
            conveyor[i + 1][0] -= 1

    # 내리는 위치는 일단 내려줌
    if conveyor[n - 1][1]:
        conveyor[n - 1][1] = False

    # 올리는 위치 확인후 로봇 올림
    if conveyor[0][0] != 0:
        conveyor[0][1] = True
        conveyor[0][0] -= 1

    # 내구도 0인 칸 카운트
    result = 0
    for i in range(2 * n):
        if conveyor[i][0] == 0:
            result += 1

    return result


input = sys.stdin.readline
n, k = map(int, input().split())
durability_info = list(map(int, input().split()))
conveyor = deque()
for i in range(2 * n):
    conveyor.append([durability_info[i], False])

count = 0
while True:
    durability_count = move_robot()
    count += 1
    if durability_count >= k:
        break
print(count)