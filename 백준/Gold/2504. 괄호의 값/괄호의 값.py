bracket = input()
stack = []
is_right = True
temp = 1
result = 0

for i in range(len(bracket)):
    if bracket[i][0] == '(':
        stack.append('(')
        temp *= 2
    elif bracket[i][0] == '[':
        stack.append('[')
        temp *= 3
    elif bracket[i][0] == ')':
        if not stack or stack[-1] == '[':
            is_right = False
            break

        if bracket[i - 1] == '(':
            result += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            is_right = False
            break

        if bracket[i - 1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if is_right and not stack:
    print(result)
else:
    print(0)