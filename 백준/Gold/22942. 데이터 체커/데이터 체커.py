import sys
input = sys.stdin.readline

n = int(input())
circle_list = []
for i in range(n):
    x, r = map(int, input().split())
    circle_list.append((x - r, i))
    circle_list.append((x + r, i))
circle_list.sort()

stack = []
for circle_info in circle_list:
    if not stack:
        stack.append(circle_info)
    else:
        if stack[-1][1] == circle_info[1]:
            stack.pop()
        else:
            stack.append(circle_info)

if not stack:
    print('YES')
else:
    print('NO')