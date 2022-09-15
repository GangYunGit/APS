import sys
sys.stdin = open('input.txt')


# 후위 연산을 위한 후위 순회 함수
def post_order(n):
    if n:
        post_order(child_left[n])       # L
        post_order(child_right[n])      # R

        # V : tree[n]의 값이 숫자일 경우에는 스택에 push
        if tree[n].isdecimal():
            stack.append(int(tree[n]))
        # v : tree[n]의 값이 숫자 이외인 경우에는 연산자에 따라 연산을 수행
        # stack 이론 시간에 배운 후위 연산법 활용
        else:
            a = stack.pop()
            b = stack.pop()

            # 주의! 꺼낸 숫자를 앞에서 계산해야 함
            if tree[n] == "+":
                stack.append(b + a)
            elif tree[n] == "-":
                stack.append(b - a)
            elif tree[n] == "*":
                stack.append(b * a)
            else:
                stack.append(b // a)


for test_case in range(1, 11):
    N = int(input())
    calculate_list = [list(input().split()) for _ in range(N)]

    tree = [''] * (N + 1)           # 연산자가 끼어있어서 트리를 빈 문자열로 초기화
    child_left = [0] * (N + 1)      # 왼쪽 자식 노드의 인덱스 정보 초기화
    child_right = [0] * (N + 1)     # 오른쪽 자식 노드의 인덱스 정보 초기화
    stack = []                      # 스택 초기화

    # 입력으로 받은 계산 정보 리스트를 돌면서 확인
    for calculate in calculate_list:

        # 리스트의 길이가 4이면
        if len(calculate) == 4:
            tree[int(calculate[0])] = calculate[1]                  # 트리의 값에 연산자를 저장
            child_left[int(calculate[0])] = int(calculate[2])       # 왼쪽 자식 노드의 인덱스를 저장
            child_right[int(calculate[0])] = int(calculate[3])      # 오른쪽 자식 노드의 인덱스를 저장

        # 리스트의 길이가 2이면 바로 트리에 값을 저장
        else:
            tree[int(calculate[0])] = calculate[1]

    post_order(1)       # 루트에서 후위 순회 진행
    print(f'#{test_case} {stack[0]}')