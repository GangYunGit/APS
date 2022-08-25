# 5102_노드의_거리

import sys
sys.stdin = open("input.txt")


# BFS 함수
def bfs(s, g):
    visited[s] = 1      # 방문 표시
    queue.append(s)     # 시작점 enQueue

    # 큐가 비어있을 때까지
    while queue:
        s = queue.pop(0)    # deQueue

        # 모든 인접 정점에 대하여
        for next_s in adj_list[s]:

            # 방문하지 않았다면 시작점으로부터의 거리 표시
            if visited[next_s] == 0:
                visited[next_s] = visited[s] + 1
                queue.append(next_s)    # 인접 정점을 enQueue

                # 도착 지점을 찾았다면 거리 반환 후 종료
                if next_s == g:
                    return visited[g] - 1

    # 도착 지점을 찾지 못하고 BFS가 끝나면 0을 반환 후 종료
    return 0


for test_case in range(1, int(input()) + 1):
    # 입력
    v, e = map(int, input().split())
    edge_list = [list(map(int, input().split())) for _ in range(e)]
    start, goal = map(int, input().split())

    # 인접 리스트 생성
    adj_list = [[] for _ in range(v + 1)]
    for v1, v2 in edge_list:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    queue = []
    visited = [0] * (v + 1)     # 방문 리스트 생성
    print(f'#{test_case} {bfs(start, goal)}')
