import sys
sys.stdin = open('input.txt')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())                # 정점의 개수, 간선의 개수
    edge_info = list(map(int, input().split()))     # 간선 정보
    parent = [_ for _ in range(N + 1)]              # make-set
    count_set = 0                                   # 그룹을 카운트해줄 변수

    for i in range(M):
        start, end = edge_info[i * 2], edge_info[i * 2 + 1]     # 간선 정보에서 시작 노드와 끝 노드를 추출
        root_start, root_end = find_set(start), find_set(end)   # find-set 으로 대표값을 찾아 저장

        if root_start != root_end:              # 서로 연결된 정점인데 대표값이 다르면
            parent[root_end] = root_start       # union 진행

    for i in range(1, N + 1):
        if parent[i] == i:      # 대표값 찾기
            count_set += 1      # 찾으면 카운트 +1

    print(f'#{test_case} {count_set}')
