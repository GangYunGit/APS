n = int(input())
num_list = [int(input()) for _ in range(n)]
num_list = num_list[::-1]
stack = []
result = []
i = 1
flag = True
while num_list:
    num_pop = 0
    stack_pop = 0
    if i <= num_list[-1]:
        stack.append(i)
        result.append('+')
        i += 1
    else:
        num_pop = num_list.pop()
        stack_pop = stack.pop()
        if num_pop == stack_pop:
            result.append('-')
        else:
            flag = False
            break

if flag:
    print(*result, sep='\n')
else:
    print('NO')