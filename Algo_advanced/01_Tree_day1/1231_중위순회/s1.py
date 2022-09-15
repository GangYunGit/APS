import sys
sys.stdin = open('input.txt')


# 중위 순회 함수
def inorder(n):
    # 선택한 정점의 자식이 존재한다면 중위 순회 진행
    if n:
        inorder(child_left[n])

        # 진호님 코드
        # result += arr[n]
        # 메인에서 결과값을 담을 배열을 선언 후 하나씩 담아서 마지막에 출력하면 더 깔끔함
        print(tree_info[n - 1][1], end='')

        inorder(child_right[n])

    return      # 자식이 없다면 리턴


for test_case in range(1, 11):
    N = int(input())
    tree_info = [input().split() for _ in range(N)]

    # 왼쪽, 오른쪽 자식노드를 초기화 (0번째 인덱스는 사용하지 않음)
    child_left = [0] * (N + 1)
    child_right = [0] * (N + 1)

    for i in range(len(tree_info)):
        # 간선에 대한 정보가 있는 입력값을 배열의 길이를 이용하여 판별
        # 완전 이진 트리의 규칙을 따름
        if len(tree_info[i]) == 3:
            child_left[int(tree_info[i][0])] = int(tree_info[i][2])     # 첫 번째 간선 정보를 왼쪽 자식노드로 사용
        elif len(tree_info[i]) == 4:
            child_left[int(tree_info[i][0])] = int(tree_info[i][2])     # 첫 번째 간선 정보를 왼쪽 자식노드로 사용
            child_right[int(tree_info[i][0])] = int(tree_info[i][3])    # 두 번째 간선 정보는 오른쪽 자식 노드로 사용

    print(f'#{test_case}', end=' ')
    inorder(1)      # 트리의 루트에서 inorder 순회 실행
    print()
