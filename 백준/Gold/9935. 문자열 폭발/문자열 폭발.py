words, bomb = input(), input()
stack = []

for word in words:
    stack.append(word)
    check = stack[len(stack) - len(bomb):]
    if "".join(check) == bomb:
        for i in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")