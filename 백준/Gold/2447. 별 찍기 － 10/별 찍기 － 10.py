def dfs(n):
    if n == 1:
        return ['*']

    former_stars = dfs(n // 3)
    now_starts = []

    for former_star in former_stars:
        now_starts.append(former_star * 3)
    for former_star in former_stars:
        now_starts.append(former_star + ' ' * (n // 3) + former_star)
    for former_star in former_stars:
        now_starts.append(former_star * 3)

    return now_starts


n = int(input())
print('\n'.join(dfs(n)))