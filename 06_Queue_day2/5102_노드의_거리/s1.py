# 5102_노드의_거리

import sys
sys.stdin = open("input.txt")


def bfs(s, g):
    visited[s] = 1
    queue.append(s)

    while queue:
        s = queue.pop()
        for next_s in adj_list[s]:
            if visited[next_s] == 0:
                visited[next_s] = visited[s] + 1
                queue.append(next_s)
                if next_s == g:
                    return visited[g] - 1

    return 0


for test_case in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    edge_list = [list(map(int, input().split())) for _ in range(e)]
    start, goal = map(int, input().split())

    adj_list = [[] for _ in range(v + 1)]
    for v1, v2 in edge_list:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    queue = []
    visited = [0] * (v + 1)
    print(f'#{test_case} {bfs(start, goal)}')
