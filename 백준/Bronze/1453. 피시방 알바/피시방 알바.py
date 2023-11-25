computer = [False] * 101
n = int(input())
count = 0
for i in list(map(int, input().split())):
    if not computer[i]:
        computer[i] = True
    else:
        count += 1
print(count)
