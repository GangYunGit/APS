# 5174_subtree

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def preorder(n):
    global count                    # 노드의 개수를 카운트해줄 변수
    if n:                           # 다음 노드가 있으면(리프 노드가 아니라면)
        count += 1                  # 전위 순회 'V'단계 : 노드 개수 카운트
        preorder(child_left[n])     # 전위 순회 'L'단계
        preorder(child_right[n])    # 전위 순회 'R'단계


for test_case in range(1, int(input()) + 1):

    edge, node = map(int, input().split())          # 간선의 개수와 노드를 입력받음
    node_list = list(map(int, input().split()))     # 노드의 정보를 입력받음

    child_left = [0] * (edge + 2)                   # 왼쪽 자식노드 정보를 초기화
    child_right = [0] * (edge + 2)                  # 오른쪽 자식노드 정보를 초기화

    for i in range(edge):
        parent, child = node_list[2 * i], node_list[2 * i + 1]

        # 부모의 왼쪽 자식노드가 비어있다면 값을 저장
        if child_left[parent] == 0:
            child_left[parent] = child

        # 왼쪽 자식노드가 존재한다면 오른쪽 자식노드에 저장
        else:
            child_right[parent] = child

    count = 0
    preorder(node)      # 전위순회 진행
    print(f'#{test_case} {count}')
