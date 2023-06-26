import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
left_heap = []
right_heap = []
for i in range(n):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heappush(left_heap, -num)
    else:
        heappush(right_heap, num)

    if right_heap and -left_heap[0] > right_heap[0]:
        left = heappop(left_heap)
        right = heappop(right_heap)
        heappush(left_heap, -right)
        heappush(right_heap, -left)
    print(-left_heap[0])