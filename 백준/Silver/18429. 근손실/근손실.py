def routine(start, end, current_big_three):
    global count
    if current_big_three < 500:
        return
    else:
        if start == len(kit):
            count += 1
            return

    for i in range(end):
        if not visited[i]:
            visited[i] = True
            routine(start + 1, end, current_big_three + kit[i] - k)
            visited[i] = False


n, k = map(int, input().split())
kit = list(map(int, input().split()))
count = 0
visited = [False] * len(kit)
routine(0, len(kit), 500)
print(count)