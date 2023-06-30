import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
meeting_list = [list(map(int, input().split())) for _ in range(n)]
meeting_list.sort()
heap = []
for start, end in meeting_list:
    if not heap:
        heap.append(end)
    else:
        if heap[0] <= start:
            heappop(heap)
            heappush(heap, end)
        else:
            heappush(heap, end)

print(len(heap))