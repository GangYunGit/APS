# p2_괄호_검사

import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input()) + 1):
    my_bracket = input()
    stack = []
    rule_break = 0
    result = 0

    for bracket in my_bracket:

        # 문자가 왼쪽 괄호라면 스택에 왼쪽 괄호를 쌓는다
        if bracket == "(":
            stack.append("(")

        # 문자가 오른쪽 괄호라면 스택에 저장된 값을 제거
        else:
            if not stack:   # 스택이 비어있는데 pop을 시도하면 조건 위반
                rule_break = 1
                break
            stack.pop()

    if not stack and rule_break != 1:
        result = 1
    else:   # 마지막까지 수행했을 때 스택이 비어있지 않으면 조건 위반
        result = -1

    print(f'#{test_case} {result}')
