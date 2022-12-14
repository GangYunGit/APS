test_case = int(input())
brackets_list = [input() for _ in range(test_case)]

for brackets in brackets_list:
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append('(')
        if bracket == ')':
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print('NO')