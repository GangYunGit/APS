import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    input_num = int(input())
    if input_num != 0:
        heappush(heap, (abs(input_num), input_num))
    else:
        try:
            print(heappop(heap)[1])
        except:
            print(0)