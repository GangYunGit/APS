# 2116_주사위_쌓기

import sys
sys.stdin = open("input.txt")

N = int(input())
side = []
face_side = []

dice_list = [list(map(int, input().split())) for _ in range(N)]

print(dice_list)

for i in range(N):
    for j in range(6):
        if j == 0 or j == 1 or j == 2:
            side.append(dice_list[i][j])
        elif j == 5 or j == 3 or j == 4:
            face_side.append(dice_list[i][j])

print(side)
print(face_side)

