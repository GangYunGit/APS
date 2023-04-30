import sys
input = sys.stdin.readline


def dfs(start, end, order):
    global is_found
    if is_found:

        return

    if len(result) == end:
        i = 0
        for sign in sign_list:
            if sign == "<":
                if result[i] > result[i + 1]:
                    return
            else:
                if result[i] < result[i + 1]:
                    return
            i += 1
        print("".join(result))
        is_found = True

    for i in order:
        if not visited[int(i)]:
            visited[int(i)] = True
            result.append(str(i))
            dfs(start + 1, end, order)
            visited[int(i)] = False
            result.pop()


k = int(input())
sign_list = list(input().split())
result = []
nums = [str(_) for _ in range(10)]
visited = [False for _ in range(10)]
is_found = False
dfs(0, k + 1, nums[::-1])
is_found = False
dfs(0, k + 1, nums)