import sys
sys.stdin = open('input.txt', encoding='utf-8')


def bfs(v):
    visited[v] = True
    depth = 1                       # 첫 번째 연락이 수행됨
    queue.append([v, depth])        # queue에 들어갈 때마다 연락의 깊이도 증가

    while queue:
        t, depth = queue.pop(0)
        for next_t in adj_list[t]:                      # 인접한 정점에 대하여
            if not visited[next_t]:                     # 방문하지 않았다면
                visited[next_t] = True                  # 방문표시를 해주고
                queue.append([next_t, depth + 1])       # queue 에 들어갈 때마다 연락의 깊이도 증가
                result.append([next_t, depth + 1])      # 노드 결과, 깊이를 저장


for test_case in range(1, 11):
    vertex_num, start = map(int, input().split())
    vertex = list(map(int, input().split()))
    adj_list = [[] for _ in range(101)]

    for i in range(0, vertex_num, 2):
        adj_list[vertex[i]].append(vertex[i + 1])

    visited = [False] * 101     # visited 배열
    queue = []                  # queue 선언
    result = []                 # 결과를 담을 배열
    bfs(start)                  # 시작지점에서 bfs 수행

    result.sort(key=lambda x: (x[1], x[0]))     # x[1] = 깊이, x[0] = 노드 번호로 오름차순
    print(f'#{test_case} {result[-1][0]}')      # 오름차순 정렬된 배열의 가장 마지막 값을 뽑으면 최대값이 나온다
