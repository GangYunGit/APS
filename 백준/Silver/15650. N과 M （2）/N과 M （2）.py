def combinations(start, end):

    if len(arr) == end:
        print(*arr)
        return

    for i in range(start, n):
        arr.append(i + 1)
        combinations(i + 1, end)
        arr.pop()


n, m = map(int, input().split())
arr = []
combinations(0, m)