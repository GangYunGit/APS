import sys
sys.stdin = open('input.txt', encoding='utf-8')


# 중위 순회 함수
def in_order(n):
    global count                    # 트리에 저장할 count 변수
    if n:                           # 노드가 존재한다면
        in_order(child_left[n])     # 중위 순회 L
        count += 1                  # 중위 순회 V 지점에서 count를 +1 해주고
        tree[n] = count             # 중위 순회 v 지점에서 트리에 count를 저장
        in_order(child_right[n])    # 중위 순회 R


for test_case in range(1, int(input()) + 1):
    N = int(input())
    tree = list(range(N + 1))
    child_left = [0] * (N + 1)
    child_right = [0] * (N + 1)

    # 부모에 대한 왼쪽 / 오른쪽 자식 노드를 생성
    for parent in range(1, N + 1):
        if parent * 2 <= N:         # 왼쪽 자식노드의 최대 인덱스를 넘어가지 않도록
            child_left[parent] = parent * 2
        if parent * 2 + 1 <= N:     # 오른쪽 자식노드의 최대 인덱스를 넘어가지 않도록
            child_right[parent] = parent * 2 + 1

    count = 0       # count 변수 초기화
    in_order(1)     # 루트에서 중위 순회 진행
    print(f'#{test_case} {tree[1]} {tree[N // 2]}')
