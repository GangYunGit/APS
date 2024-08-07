# BOJ_1377. 버블 소트

import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for i in range(N):
    num_list.append((int(input()), i))

sorted_list = sorted(num_list)
max_count = 0

for i in range(N):
    max_count = max(max_count, sorted_list[i][1] - i)

print(max_count + 1)

'''
7
3
3
3
1
4
6
8

'''
