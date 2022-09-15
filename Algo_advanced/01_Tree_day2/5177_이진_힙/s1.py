import sys
sys.stdin = open('input.txt')


# 힙에 숫자를 삽입하는 함수
def heap_push(n):
    global last             # 일단 힙에 값을 넣어줄 인덱스 변수를 설정
    last += 1               # 완전 이진 트리의 순서에 맞도록 인덱싱
    heap[last] = n          # 지금 보고있는 인덱스에 push

    child = last            # 지금 보고있는 인덱스를 자식 노드로 삼는다
    parent = child // 2     # 부모 노드는 자식 노드의 절반(flow 연산)

    # 부모 노드가 존재하며, 최소 힙의 조건에 맞지 않다면 맞을 때까지 수행
    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]   # 부모 노드와 자식 노드를 교환
        child = parent          # 반복문의 조건에 걸려서 부모와 자식이 교환되었다면 인덱스도 같이 바꿔준다.
        parent = child // 2     # 바뀐 자식의 인덱스와 부모의 인덱스를 맞추어준다.


for test_case in range(1, int(input()) + 1):
    N = int(input())
    nodes = list(map(int, input().split()))

    heap = [0] * (N + 1)
    result = 0
    last = 0

    # 노드의 값들을 힙에 삽입
    for node in nodes:
        heap_push(node)

    # 리프 노드의 마지막 인덱스 저장
    last_node_idx = len(heap) - 1

    # 부모노드를 루트가 나올 때까지 찾아감
    while last_node_idx != 1:
        last_node_idx //= 2
        result += heap[last_node_idx]   # 찾은 값을 더해서 결과에 반영

    print(f'#{test_case} {result}')
