from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', encoding='utf-8')


def prim(start):
    visited = [False] * (N + 1)
    heap = [(0, start)]
    cost = 0

    while heap:
        min_distance, min_node = heappop(heap)
        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_distance

        # 인접 정점에 대해 가중치의 정점 정보를 힙에 삽입
        for next_node, w in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (w, next_node))

    return cost

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))