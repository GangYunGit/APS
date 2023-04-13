from heapq import heappop, heappush

N = int(input())
heap = []
for _ in range(N):
    heappush(heap, int(input()))

for _ in range(N):
    print(heappop(heap))
