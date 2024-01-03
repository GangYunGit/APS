def dfs():

    if sum(pick) > n:
        return
    elif sum(pick) == n:
        temp = [str(pick[i]) for i in range(len(pick))]
        result.append("+".join(temp))
        return

    for i in range(1, 4):
        pick.append(i)
        dfs()
        pick.pop()


n, k = map(int, input().split())
pick = []
result = []
dfs()
result.sort()
if 0 < k <= len(result):
    print(result[k - 1])
else:
    print(-1)