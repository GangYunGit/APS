# 2564_경비원

import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
N = int(input())
store_info = [list(map(int, input().split())) for _ in range(N)]
my_location = list(map(int, input().split()))
min_distance = 0

print(store_info)
print(my_location)

for direction, distance in store_info:
    if my_location[0] == 1:
        if direction != 2:
            min_distance +=



print(min_distance)
# 상점이 북, 남에 위치한 경우
# x, y좌표로 생각해서 풀어볼까?