#  1210_Ladder 1

import sys
sys.stdin = open("input.txt")

T = int(input())

dx = [0, 0, -1, 1]  # ----- 상 하
dy = [-1, 1, 0, 0]  # 좌 우 -----

for test_case in range(1, 2):
    ladder = [list(map(int, input().split())) for i in range(100)]
    x_start, y_start, x_end, y_end = 99, 99, 0, 0
    direction = 2

    for x in range(100):
        for y in range(100):
            if ladder[x][y] == 2:
                x_end = x   # 99
                y_end = y   # 57

    while x_end != 0:
        x_end += dx[direction]
        y_end += dy[direction]
        print(x_end, y_end)
        # 0 = 좌 / 1 = 우 / 2 = 상 / 3 = 하

