# 2606_바이러스

import sys
sys.stdin = open("input.txt")


def bfs(v):
    global count        # 감염된 컴퓨터 수 카운트
    visited[v] = 1      # 방문했다고 표시
    queue.append(v)     # 현재 정점을 큐에 enQueue

    # 큐가 빌 때까지 반복
    while queue:
        t = queue.pop(0)     # 큐에서 deQueue한 정점을 t로 설정

        # 모든 인접 정점에 대하여
        for next_t in adj_list[t]:
            # 인접 정점을 방문하지 않았다면
            if not visited[next_t]:
                visited[next_t] = 1     # 방문했다고 표시
                queue.append(next_t)    # 해당 정점을 큐에 enQueue
                count += 1


# 입력
vertex = int(input())
edge = int(input())
v_list = [list(map(int, input().split())) for _ in range(edge)]

# 인접 리스트 생성
adj_list = [[] for _ in range(vertex + 1)]
for v1, v2 in v_list:
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

# 방문 리스트 초기화, 빈 큐 생성, 카운트 초기화, bfs 진행
visited = [0] * (vertex + 1)
queue = []
count = 0
bfs(1)

print(count)

