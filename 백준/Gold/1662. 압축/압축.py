s = input()
stack = []
result = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append((result - 1, int(s[i - 1])))
        result = 0
    elif s[i] == ")":
        temp = stack.pop()
        result *= temp[1]
        result += temp[0]
    else:
        result += 1

print(result)