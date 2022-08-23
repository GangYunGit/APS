# 4874_Forth

import sys
sys.stdin = open("input.txt")


def rank(tk):
    my_rank = 0
    if tk in "+-":
        my_rank = 1
    if tk in "*/":
        my_rank = 2
    return my_rank


for test_case in range(1, int(input()) + 1):
    postfix = input().split()
    stack = []
    result_num = 0
    result = ''

    for token in postfix:

        # 연산자를 만나면
        if token in "+-*/":

            # 숫자 2개를 꺼내야하는데 스택에 한개만 있다면 error
            if len(stack) == 1:
                result = 'error'
                break

            # 아니라면 연산자에 따라 계산 진행
            else:
                num1 = stack.pop()
                num2 = stack.pop()
            if token == "+":
                stack.append(num2 + num1)
            elif token == "-":
                stack.append(num2 - num1)
            elif token == "*":
                stack.append(num2 * num1)
            elif token == "/":
                if num1 == 0:   # zero division error 방지
                    result = 'error'
                    break
                stack.append(num2 // num1)

        # .을 만나면 연산을 끝내고 출력
        elif token == ".":

            # 스택에 원소가 하나만 남아있어야 정상적인 연산으로 판별
            # **이거 때문에 테스트 케이스 하나가 계속 틀렸음 ㅠㅠ
            if len(stack) == 1:
                result_num = stack.pop()
                result = str(result_num)

            # 스택에 원소가 없거나 2개 이상이면 형식이 잘못됨
            else:
                result = 'error'

        # 숫자를 만나면 스택에 저장
        else:
            stack.append(int(token))

    print(f'#{test_case} {result}')
