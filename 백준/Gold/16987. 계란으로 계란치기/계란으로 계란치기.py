import sys


def dfs(current_idx, count):
    global max_count
    max_count = max(max_count, count)

    if current_idx == n:
        return

    for i in range(n):
        if i != current_idx:
            if egg_info[i][0] > 0 and egg_info[current_idx][0] > 0:
                break_count = 0
                egg_info[i][0] -= egg_info[current_idx][1]
                egg_info[current_idx][0] -= egg_info[i][1]
                if egg_info[i][0] <= 0:
                    break_count += 1
                if egg_info[current_idx][0] <= 0:
                    break_count += 1
                count += break_count
                dfs(current_idx + 1, count)

                egg_info[i][0] += egg_info[current_idx][1]
                egg_info[current_idx][0] += egg_info[i][1]
                count -= break_count
            else:
                dfs(current_idx + 1, count)

    return count


input = sys.stdin.readline
n = int(input())
egg_info = [list(map(int, input().split())) for _ in range(n)]
max_count = 0
dfs(0, 0)
print(max_count)