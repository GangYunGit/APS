import sys
sys.stdin = open('input.txt')


# 전위순회 함수
def preorder_counter(v):
    global count
    if v:                       # v가 0이 아닌 경우 수행
        count += 1               # 방문한 지점을 출력
        preorder_counter(child_left[v])    # 왼쪽 자식노드를 탐색
        preorder_counter(child_right[v])    # 오른쪽 자식노드를 탐색

    return  # if문에 걸리지 않으면 호출 스택에서 해제


# 전위순회 함수
def preorder(v):
    if v:                       # v가 0이 아닌 경우 수행
        print(v, end=' ')                # 방문한 지점을 출력
        preorder(child_left[v])    # 왼쪽 자식노드를 탐색
        preorder(child_right[v])    # 오른쪽 자식노드를 탐색

    return  # if문에 걸리지 않으면 호출 스택에서 해제


def inorder(v):
    if v:                       # v가 0이 아닌 경우 수행
        inorder(child_left[v])    # 왼쪽 자식노드를 탐색
        print(v, end=' ')  # 방문한 지점을 출력
        inorder(child_right[v])    # 오른쪽 자식노드를 탐색

    return  # if문에 걸리지 않으면 호출 스택에서 해제


def postorder(v):
    if v:                       # v가 0이 아닌 경우 수행
        postorder(child_left[v])    # 왼쪽 자식노드를 탐색
        postorder(child_right[v])    # 오른쪽 자식노드를 탐색
        print(v, end=' ')  # 방문한 지점을 출력

    return  # if문에 걸리지 않으면 호출 스택에서 해제


vertex = int(input())
arr = list(map(int, input().split()))
edge = vertex - 1

# 정점이 1부터 시작하므로 인덱스를 1 늘려줌
child_left = [0] * (vertex + 1)
child_right = [0] * (vertex + 1)

# 부모 인덱스를 기준으로 자식을 구함
for i in range(edge):
    parent, child = arr[2 * i], arr[2 * i + 1]

    # 왼쪽 자식노드가 비어있으면 추가
    if child_left[parent] == 0:
        child_left[parent] = child

    # 왼쪽 자식노드에 값이 있다면 오른쪽 자식노드에 추가
    else:
        child_right[parent] = child

start = 1
preorder(start)
print()
inorder(start)
print()
postorder(start)
print()

count = 0
preorder_counter(3)
print(count)