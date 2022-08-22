# 계산기 1

import sys
sys.stdin = open('input.txt')


# 연산자들의 우선순위를 정할 함수
def rank(s):
    if s in "+-":
        return 1
    elif s in "*/":
        return 2


for test_case in range(1, int(input()) + 1):
    calculate = input()
    cal_stack = []

    # 주어진 식을 한 글자씩 순회
    for token in calculate:

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
