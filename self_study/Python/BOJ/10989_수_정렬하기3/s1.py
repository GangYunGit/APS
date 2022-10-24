import sys
input = sys.stdin.readline

N = int(input())
num_list = [0] * 10001

for i in range(N):
    num_list[int(input())] += 1

for i in range(1, 10001):
    if num_list[i] > 0:
        for j in range(num_list[i]):
            print(i)
