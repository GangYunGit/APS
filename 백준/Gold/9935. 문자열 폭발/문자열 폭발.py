words, bomb = input(), list(input().rstrip())
stack = []
bomb_length = len(bomb)

for word in words:
    stack.append(word)
    if stack[-bomb_length:] == bomb:
        for i in range(bomb_length):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")