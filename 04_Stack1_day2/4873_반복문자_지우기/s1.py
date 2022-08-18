# 4873_반복문자_지우기

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    my_str = input()
    stack = [my_str[0]]

    # 첫 글자가 스택에 들어간 상태로 다음 글자부터 반복문을 진행
    for i in range(1, len(my_str)):
        # 반복을 하는 동안 스택이 비어있으면 공백문자로 인식하도록 설정
        if len(stack) == 0:
            str_search = ''
        # 스택의 가장 최신 문자를 저장
        else:
            str_search = stack[len(stack) - 1]

        # 스택의 가장 최신 문자와 문자열의 값이 다르면 스택에 추가
        if str_search != my_str[i]:
            stack.append(my_str[i])
        # 스택의 가장 최신 문자와 문자열의 값이 같으면 pop
        else:
            stack.pop()

    print(f'#{test_case} {len(stack)}')




