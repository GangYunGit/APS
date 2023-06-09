word = input()
stack = []

for i in range(len(word)):
    stack.append(word[i])
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(4):
            stack.pop()
        stack.append('P')

if stack == ['P']:
    print('PPAP')
else:
    print('NP')