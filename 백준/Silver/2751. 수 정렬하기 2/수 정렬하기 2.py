from heapq import heappush, heappop
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    heappush(heap, int(input()))
for _ in range(n):
    print(heappop(heap))
