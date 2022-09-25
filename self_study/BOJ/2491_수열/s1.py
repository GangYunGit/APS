# 2491_수열
import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = list(map(int, input().split()))
up_count = 1
up_counter = []
down_count = 1
down_counter = []

if N == 1:
    result = 1

else:
    for i in range(N - 1):
        if num_list[i] <= num_list[i + 1]:
            up_count += 1
        else:
            up_count = 1
        up_counter.append(up_count)

        if num_list[i] >= num_list[i + 1]:
            down_count += 1
        else:
            down_count = 1
        down_counter.append(down_count)

    max_up = max(up_counter)
    max_down = max(down_counter)
    result = max(max_up, max_down)

print(result)

