# 1224_계산기3

import sys
sys.stdin = open("input.txt")


# 연산자의 우선순위를 지정하는 함수
def rank(token):
    my_rank = 0
    if token in "(":
        my_rank = 0
    if token in "+-":
        my_rank = 1
    if token in "*/":
        my_rank = 2
    return my_rank


for test_case in range(1, 11):
    N = int(input())
    calculate = input()
    stack = []
    postfix = ''

    # ---------------- 후위 표기법으로 바꾸는 과정 -----------------
    for token in calculate:

        # 연산자를 만났을 때
        if token in "+_*/(":

            # 스택이 비어있거나, 여는 괄호를 만났다면 push
            if not stack or token == "(":
                stack.append(token)

            # 토큰의 연산 우선순위가 스택 top 값의 우선순위보다 높으면 push
            elif rank(token) > rank(stack[-1]):
                stack.append(token)

            # 토큰의 연산 우선순위가 스택 top 값의 우선순위보다 낮으면 더 높은 우선순위를 가진 연산자를 만날 때까지 pop
            elif rank(token) <= rank(stack[-1]):
                while stack and (rank(stack[-1]) >= rank(token)):
                    postfix += stack.pop()
                stack.append(token)     # 더 높은 우선순위의 연산자를 push

        # 닫는 괄호를 만나면
        elif token == ")":

            # 스택에서 여는 괄호를 만날 때까지 스택에 들어있는 연산자를 pop
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()     # 연산자를 모두 pop 하고 남아있는 "("를 스택에서 삭제

        # 수식에서 숫자를 만나면 결과에 저장
        else:
            postfix += token

    # 스택에 남아있는 연산자가 있다면 pop
    while stack:
        postfix += stack.pop()
    # ----------------------------------------------------------------

    # ---------------- 후위 표기법으로 바꾼 수식 계산 -----------------
    calculation_stack = []
    for token in postfix:

        # 연산자를 만나면 스택에 저장된 숫자 2개를 꺼내서 연산 수행
        if token in "+_*/":
            num_1 = calculation_stack.pop()
            num_2 = calculation_stack.pop()
            if token == "+":
                calculation_stack.append(num_2 + num_1)
            elif token == "-":
                calculation_stack.append(num_2 - num_1)
            elif token == "*":
                calculation_stack.append(num_2 * num_1)
            elif token == "/":
                calculation_stack.append(num_2 / num_1)

        # 숫자를 만나면 스택에 push
        else:
            calculation_stack.append(int(token))

    print(f'#{test_case} {calculation_stack[-1]}')
