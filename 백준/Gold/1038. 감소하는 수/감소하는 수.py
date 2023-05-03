def dfs(start):
    global count
    for j in range(1, 11):
        if len(num) == j and num == sorted(num):
            result.append(int("".join(num)[::-1]))
            count += 1

    if len(num) == 10:
        return

    for i in range(start, 10):
        num.append(str(i))
        dfs(i + 1)
        num.pop()


count = 0
n = int(input())
num = []
result = []
dfs(0)
result = sorted(result)
if n < 1023:
    print(result[n])
else:
    print(-1)