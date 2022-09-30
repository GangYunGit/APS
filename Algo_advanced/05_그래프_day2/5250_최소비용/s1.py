# 5250_최소비용

import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')


# 좌, 상, 우, 하
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
INF = 100 * 100 * 1000


def dijkstra(start):
    distance[start[0]][start[1]] = 0
    heap = [(0, start)]

    while heap:
        # 최단거리가 가장 짧은 좌표를 선택
        min_distance, min_node = heappop(heap)

        # 최단거리 후보들보다 크다면 무시
        if distance[min_node[0]][min_node[1]] > min_distance:
            continue

        # 델타 검색 수행
        for k in range(4):
            n_i = min_node[0] + di[k]
            n_j = min_node[1] + dj[k]

            # 다음 좌표가 범위 내에 있다면
            if 0 <= n_i < N and 0 <= n_j < N:
                # 일단 다음 지역으로 넘어가려면 비용 1이 필요한데
                next_distance = min_distance + 1

                # 다음 지역이 현재 지역보다 높으면
                if height_list[n_i][n_j] > height_list[min_node[0]][min_node[1]]:
                    # 다음 지역과 현재 지역의 차이만큼 비용 추가
                    next_distance += height_list[n_i][n_j] - height_list[min_node[0]][min_node[1]]

                # 다음 지역으로 이동하기 위한 비용이 저장되어있는 비용보다 작다면 최소비용임
                if next_distance < distance[n_i][n_j]:
                    distance[n_i][n_j] = next_distance
                    heappush(heap, (next_distance, (n_i, n_j)))


for test_case in range(1, int(input()) + 1):
    N = int(input())
    height_list = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    start_node = (0, 0)
    dijkstra(start_node)
    print(f'#{test_case} {distance[N - 1][N - 1]}')
