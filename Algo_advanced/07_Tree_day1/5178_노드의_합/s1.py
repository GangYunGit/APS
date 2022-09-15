# 5178_노드의 합

import sys
sys.stdin = open('input.txt', encoding='utf-8')


# 후위 순회 함수
def post_order(n):
    if n:
        post_order(child_left[n])       # L
        post_order(child_right[n])      # R
        tree[n] = child_left[n * 2] + child_right[n * 2 + 1]    # V : 자식 노드들의 합을 부모에 저장

        # n이 홀수 일 때에는 오른쪽 자식 노드의 값이 다시 부모노드가 됨
        if n % 2:
            child_right[n] = tree[n]

        # n이 짝수 일 때에는 왼쪽 자식 노드의 값이 다시 부모노드가 됨
        else:
            child_left[n] = tree[n]


for test_case in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    leaf_node_info = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N + 1)            # 트리 초기화
    child_left = [0] * (N + 2)      # 왼쪽 자식노드 배열 초기화
    child_right = [0] * (N + 2)     # 오른쪽 자식노드 배열 초기화

    # 입력된 노드정보를 이용하여 리프노드만 저장된 트리를 만든다
    for node_num, value in leaf_node_info:
        tree[node_num] = value

    for idx in range(1, N + 1):
        # 트리가 비어있지 않으면
        if tree[idx] != 0:
            # 트리의 인덱스가 홀수이면 오른쪽 자식노드에 저장
            if idx % 2 == 1:
                child_right[idx] = tree[idx]
            # 트리의 인덱스가 짝수이면 왼쪽 자식노드에 저장
            else:
                child_left[idx] = tree[idx]

    # 비어있는 Tree의 인덱스 중 가장 큰 인덱스를 시작으로 후위 순회를 진행하며 값을 채워 나감
    for i in range(N // 2, 0, -1):
        post_order(i)

    print(f'#{test_case} {tree[L]}')


