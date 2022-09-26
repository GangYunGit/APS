import sys
sys.stdin = open('input.txt')


# 전위순회 함수
def pre_order(n):
    if n:
        pre_order_list.append(n)    # V
        pre_order(child_left[n])    # L
        pre_order(child_right[n])   # R


# 중위순회 함수
def in_order(n):
    if n:
        in_order(child_left[n])     # L
        in_order_list.append(n)     # V
        in_order(child_right[n])    # R


# 후위순회 함수
def post_order(n):
    if n:
        post_order(child_left[n])   # L
        post_order(child_right[n])  # R
        post_order_list.append(n)   # V


vertex = int(input())                           # 노드의 개수
edge_list = list(map(int, input().split()))     # 간선 정보

child_left = [0] * (vertex + 1)                 # 왼쪽 자식 배열 초기화
child_right = [0] * (vertex + 1)                # 오른쪽 자식 배열 초기화

for i in range(vertex - 1):
    # 간선 정보에서 부모와 자식을 추출
    parent, child = edge_list[i * 2], edge_list[i * 2 + 1] 

    if child_left[parent] == 0:         # 왼쪽 자식이 채워져있지 않으면
        child_left[parent] = child      # 넣고
    else:                               # 왼쪽 자식이 채워져 있는데 또?
        child_right[parent] = child     # 그럼 오른쪽 자식에 넣기

pre_order_list = []         # 전위 순회 결과를 담을 배열
in_order_list = []          # 중위 순회 결과를 담을 배열
post_order_list = []        # 후위 순회 결과를 담을 배열

pre_order(1)                # 전위 순회 진행
in_order(1)                 # 중위 순회 진행
post_order(1)               # 후위 순회 진행

print(pre_order_list)
print(in_order_list)
print(post_order_list)




