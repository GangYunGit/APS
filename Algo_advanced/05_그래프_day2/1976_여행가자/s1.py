# 1976_여행가자

import sys
sys.stdin = open('input.txt', encoding='utf-8')


# find-set 함수
def find_set(node):
    if node != parent[node]:                    # 부모노드 번호가 노드의 번호와 같다 == 대표값이다
        parent[node] = find_set(parent[node])   # 대표값이 아니면 find-set을 다시 적용하여 대표값을 찾아나간다
    return parent[node]                         # path-compression 으로 루트를 찾는 시간 단축!


# Union 함수
def union(node_1, node_2):
    # find-set을 해서 대표값을 찾는다(서로 소인 집합인지 확인하기 위해)
    root_1, root_2 = find_set(node_1), find_set(node_2)
    if root_1 != root_2:                # 대표값이 다르면 == 서로소이면
        if root_1 < root_2:             # 루트가 작은 원소를 대표값으로 설정하도록 함
            parent[root_2] = root_1     # union 진행
        else:
            parent[root_1] = root_2


N = int(input())
M = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
travel_plan = list(map(int, input().split()))

parent = [_ for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == 1:
            union(i + 1, j + 1)

for i in range(len(travel_plan) - 1):
    # 바로 앞뒤의 원소를 서로 비교하면서 대표값이 일치하면 == 집합에 속하는 원소이면 YES
    if find_set(travel_plan[i]) == find_set(travel_plan[i + 1]):
        result = 'YES'
    # 아니면 NO
    else:
        result = 'NO'
        break

print(result)
