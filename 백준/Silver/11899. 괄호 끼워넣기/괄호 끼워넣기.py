brackets = input()
stack = []

for bracket in brackets:
    if not stack:
        stack.append(bracket)
    else:
        if stack[-1] == '(':
            if bracket == ')':
                stack.pop()
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)
print(len(stack))