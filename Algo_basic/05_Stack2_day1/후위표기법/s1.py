# 후위 표기법

import sys
sys.stdin = open('input.txt')


# 연산자들의 우선순위를 정할 함수
def rank(s):
    if s in "()":
        return 0
    elif s in "+-":
        return 1
    elif s in "*/":
        return 2


for test_case in range(1, int(input()) + 1):
    calculate = input()
    stack = []
    result = ''

    # 주어진 수식을 한 글자씩 순회
    for token in calculate:

        # 수식에서 토큰을 발견(")" 제외) 하면
        if token in "+-*/(":

            # 스택에 없으면 일단 push
            if not stack or token == "(":
                stack.append(token)

            # 토큰의 순위가 스택의 top에 있는 토큰의 순위보다 높으면 push
            elif rank(token) > rank(stack[-1]):
                stack.append(token)

            # 토큰의 순위가 스택의 top에 있는 토큰의 순위보다 같거나 낮으면 pop
            elif rank(token) <= rank(stack[-1]):
                while stack and (rank(stack[-1]) >= rank(token)):
                    result += stack.pop()
                stack.append(token)

        # 수식에서 ")"를 발견하면
        elif token == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()

        # 수식에 숫자가 있으면 그대로 출력
        else:
            result += token

    # 스택에 남아있는 연산자를 뒤에 붙여줌
    while stack:
        result += stack.pop()

    print(f'#{test_case} {result}')
