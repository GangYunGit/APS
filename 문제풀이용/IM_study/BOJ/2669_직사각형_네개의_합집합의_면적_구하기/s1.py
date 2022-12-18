# 2669_직사각형 네개의 합집합의 면적 구하기
import sys
sys.stdin = open("input.txt")

square_info = [list(map(int, input().split())) for _ in range(4)]
grid = [[0] * 100 for _ in range(100)]
sum_square = 0
for num in range(4):
    for i in range(square_info[num][1], square_info[num][3]):
        for j in range(square_info[num][0], square_info[num][2]):
            grid[i][j] += 1

for i in range(100):
    for j in range(100):
        if grid[i][j] > 0:
            sum_square += 1

print(sum_square)



