# 1922_네트워크 연결

import sys
sys.stdin = open('input.txt', encoding='utf-8')
input = sys.stdin.readline


# find_set 함수
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


# union 을 이용하여 대표값이 다르면 사이클이 아니라고 판별
def is_not_cycle(node_1, node_2):
    root_1, root_2 = find_set(node_1), find_set(node_2)
    if root_1 != root_2:
        if root_1 < root_2:
            parent[root_2] = root_1
        else:
            parent[root_1] = root_2
        return True
    else:
        return False


N = int(input())
M = int(input())
computer_info = [list(map(int, input().split())) for _ in range(M)]
computer_info.sort(key=lambda x: x[2])

parent = [_ for _ in range(N + 1)]
cost = 0
count = 0

for start, end, distance in computer_info:
    # 사이클이 생기지 않는 원소이면 MST에 추가
    if is_not_cycle(start, end):
        count += 1          # MST's 원소의 개수를 파악
        cost += distance    # 비용을 더해줌

        if count == N - 1:  # MST가 정점의 개수만큼 찼다면
            break           # 탈출
print(cost)




