# 4866_괄호검사

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    my_string = input()
    stack = []
    result = 0

    for char in my_string:
        # 스택이 비어있는데 닫는 괄호가 먼저 나오는 경우
        if not stack:
            if char == "}" or char == ")":
                result = 0
                break

        # 왼쪽 괄호는 종류별로 스택에 쌓는다
        if char == "{":
            stack.append("{")
        elif char == "(":
            stack.append("(")

        # 중괄호를 제거하고 싶은데 스택에서 나온 값이 소괄호라면 조건 위반
        if char == "}":
            bracket_pop = stack.pop()
            if bracket_pop == "(":
                result = 0
                break

        # 소괄호를 제거하고 싶은데 스택에서 나온 값이 중괄호라면 조건 위반
        if char == ")":
            bracket_pop = stack.pop()
            if bracket_pop == "{":
                result = 0
                break

        # 마지막까지 수행했을 때 스택이 비어있으면 조건 충족, 아니면 조건 위반
        if char == my_string[len(my_string) - 1]:
            if not stack:
                result = 1
            else:
                result = 0

    print(f'#{test_case} {result}')