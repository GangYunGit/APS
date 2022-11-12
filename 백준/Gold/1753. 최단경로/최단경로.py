import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 100000000


def dijkstra(node):
    distance[node] = 0
    # 힙 초기화 : (거리, 정점)
    heap = [(0, node)]

    # for end, weight in graph[node]:
    #     distance[end] = weight
    #
    # for _ in range(edge - 1):
    #     # 최단 거리가 확정되지 않은 정점들 중 최단 거리가 가장 짧은 정점을 선택
    #     min_distance = INF
    #     for i in range(1, vertex + 1):
    #         if not visited[i] and min_distance > distance[i]:
    #             min_node = i
    #             min_distance = distance[min_node]

    while heap:
        min_distance, min_node = heappop(heap)

        # 최단거리 후보들보다 크다면 무시
        if distance[min_node] > min_distance:
            continue

        # 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_end, next_weight in graph[min_node]:
            next_distance = min_distance + next_weight
            if next_distance < distance[next_end]:
                distance[next_end] = next_distance
                heappush(heap, (next_distance, next_end))


vertex, edge = map(int, input().split())
start_node = int(input())
edge_list = [list(map(int, input().split())) for _ in range(edge)]

distance = [INF] * (vertex + 1)
graph = [[] for _ in range(vertex + 1)]
for start, end, weight in edge_list:
    graph[start].append((end, weight))

dijkstra(start_node)

for i in range(1, vertex + 1):
    if distance[i] == INF :
        print('INF')
    else:
        print(distance[i], end='\n')
