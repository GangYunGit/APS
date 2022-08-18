# 1234_비밀번호

import sys
sys.stdin = open("input.txt")

for test_case in range(1, 11):
    # password를 문자열의 형태로 받는다.(0으로 시작하여 데이터가 소실되는 것을 방지)
    N, password = map(str, input().split())
    stack = []
    password = str(password)

    for i in range(len(password)):
        # 스택이 비어있으면 push
        if not stack:
            stack.append(password[i])

        # 이후 append를 진행하면서 이전의 문자와 동일한 문자가 들어왔다면 pop을 2번 시행
        else:
            stack.append(password[i])
            if stack[len(stack) - 1] == stack[len(stack) - 2]:
                stack.pop()
                stack.pop()

    print(f'#{test_case }', end=' ')
    print(*stack, sep='')
