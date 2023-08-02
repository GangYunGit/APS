def func(arr):
    result = 0
    for i in range(len(arr) - 1):
        result += abs(arr[i] - arr[i + 1])
    return result


def comb():
    global max_sum

    if len(pick) == n:
        max_sum = max(func(pick), max_sum)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            pick.append(a[i])
            comb()
            pick.pop()
            visited[i] = False


n = int(input())
a = list(map(int, input().split()))
visited = [False for _ in range(n)]
pick = []
max_sum = 0
comb()
print(max_sum)