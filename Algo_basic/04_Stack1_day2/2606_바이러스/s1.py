# 2606_바이러스

import sys
sys.stdin = open("input.txt")


def dfs(v):
    visited[v] = True   # v를 방문했다는 표시
    stack = [v]         # 스택에 v를 쌓고 시작

    while stack:        # 스택이 비어있을 때까지 진행
        v = stack.pop()     # v 지점과 인접한 정점들에 대한 반복을 시행할 것임
        for next_v in adj_list[v]:      # v지점과 인접한 모든 정점에 대하여
            if not visited[next_v]:     # 그 지점들을 방문 하지 않았다면
                global count
                count += 1
                visited[next_v] = True  # 방문하고 방문했다는 표시를 남김

                # 방문한 지점을 스택에 쌓음
                # 스택의 가장 위에 있는 값이 다음 반복문에서 사용된다.
                stack.append(next_v)


vertex = int(input())
N = int(input())

# 인접 리스트 초기화
adj_list = [[] for _ in range(vertex + 1)]
for i in range(N):
    v_1, v_2 = map(int, input().split())
    adj_list[v_2].append(v_1)
    adj_list[v_1].append(v_2)

# 방문 리스트 생성. 시작이 1부터이기 때문에 index를 맞추기 위해 +1
visited = [False] * (vertex + 1)
count = 0   # 감염된 컴퓨터의 수
dfs(1)      # 1번 컴퓨터에서 감염 시작

print(count)
