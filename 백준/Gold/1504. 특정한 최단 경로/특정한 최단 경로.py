from heapq import heappop, heappush


def dijkstra(start, end):
    distance = [INF] * (vertex + 1)
    distance[start] = 0
    heap = [(0, start)]     # 거리, 노드

    while heap:
        min_distance, min_node = heappop(heap)

        if distance[min_node] < min_distance:
            continue

        for next_node, next_weight in graph[min_node]:
            next_distance = min_distance + next_weight
            if next_distance < distance[next_node]:
                distance[next_node] = next_distance
                heappush(heap, (next_distance, next_node))

    return distance[end]


def search_min(v1, v2):
    distance = 0
    distance += dijkstra(1, v1)
    distance += dijkstra(v1, v2)
    distance += dijkstra(v2, vertex)
    return distance

vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
INF = 200000 * 1000
result_p1 = 0
result_p2 = 0

for i in range(edge):
    v1, v2, d = list(map(int, input().split()))
    graph[v1].append((v2, d))
    graph[v2].append((v1, d))

p1, p2 = map(int, input().split())

distance1 = search_min(p1, p2)
distance2 = search_min(p2, p1)

if distance1 >= INF and distance2 >= INF:
    print(-1)
else:
    if distance1 < distance2:
        print(distance1)
    else:
        print(distance2)