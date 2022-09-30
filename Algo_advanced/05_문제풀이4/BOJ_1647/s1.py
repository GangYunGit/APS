# 1647_도시 분할 계획

from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', encoding='utf-8')
INF = 1000 * 1000000


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]



vertex, edge = map(int, input().split())

edge_info = [list(map(int, input().split())) for _ in range(edge)]
adj_list = [[] for _ in range(vertex + 1)]

parent = [_ for _ in range(vertex + 1)]

for start, end, weight in edge_info:
    adj_list[start].append((end, weight))
    adj_list[end].append((start, weight))

