# 5251_최소 이동 거리

from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', encoding='utf-8')

INF = 10 * 1000000


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]     # 거리, 노드

    while heap:
        # 탐색할 최단 거리를 선택
        min_distance, min_node = heappop(heap)

        # 최단 거리 후보가 이미 저장되어있는 값보다 크다면 무시
        if distance[min_node] < min_distance:
            continue

        # 최단 거리 후보가 결정되었다면 그 후보의 다음 노드를 탐색
        for next_node, next_weight in graph[min_node]:
            # 다음의 최단거리를 비교하기위해 next_distance 에 다음 후보값을 저장
            next_distance = min_distance + next_weight
            # 다음 후보가 해당 노드에 이미 저장되어있는 값보다 작다면 최소거리를 갱신
            if next_distance < distance[next_node]:
                distance[next_node] = next_distance
                heappush(heap, (next_distance, next_node))


for test_case in range(1, int(input()) + 1):
    vertex, edge = map(int, input().split())
    edge_list = [list(map(int, input().split())) for _ in range(edge)]

    graph = [[] for _ in range(vertex + 1)]

    for start, end, weight in edge_list:
        graph[start].append((end, weight))

    distance = [INF] * (vertex + 1)
    dijkstra(0)
    print(f'#{test_case} {distance[-1]}')