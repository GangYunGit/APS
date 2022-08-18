# p1_스택_구현하기

my_stack = [0] * 3
top = -1

top += 1
my_stack[top] = 1

top += 1
my_stack[top] = 'a'

top += 1
my_stack[top] = 'ssafy'

print(my_stack)     # 스택에 값이 잘 들어갔는지 확인

print(my_stack.pop(), my_stack, end='')
print()
top -= 1

print(my_stack.pop(), my_stack, end='')
print()
top -= 1

# 마지막에 my_stack을 프린트해보면 비어있는 배열이 나오는 것을 볼 수 있다.
print(my_stack.pop(), my_stack, end='')
print()
top -= 1


