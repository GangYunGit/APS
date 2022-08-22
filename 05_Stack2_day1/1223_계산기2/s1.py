# 계산기 2

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


for test_case in range(1, 11):
    N = int(input())
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

    cal_stack = []
    # 주어진 식을 한 글자씩 순회
    for token in result:

        # 연산자를 찾으면
        if token in "+-*/":

            # 가장 최근의 숫자 2개를 스택에서 pop
            num_1 = cal_stack.pop()
            num_2 = cal_stack.pop()

            # 연산 진행
            if token == "+":
                cal_stack.append(num_2 + num_1)
            elif token == "-":
                cal_stack.append(num_2 - num_1)
            elif token == "*":
                cal_stack.append(num_2 * num_1)
            elif token == "/":
                cal_stack.append(num_2 / num_1)

        # 숫자를 찾으면 스택에 push
        else:
            cal_stack.append(int(token))

    print(f'#{test_case} {cal_stack[-1]}')    # 스택의 마지막 숫자를 pop

