import sys
input = sys.stdin.readline


def dfs(i, j):
    global m, count, max_count

    for k in range(len(milk_list)):
        milk_i, milk_j = milk_list[k]
        distance = abs(milk_i - i) + abs(milk_j - j)
        if country[milk_i][milk_j] == 2:
            if m >= distance:
                count += 1
                country[milk_i][milk_j] = 0
                m -= distance
                m += h
                dfs(milk_i, milk_j)

                # 백트래킹
                count -= 1
                country[milk_i][milk_j] = 2
                m += distance
                m -= h

        elif country[milk_i][milk_j] == 1:
            if m >= distance:
                max_count = max(count, max_count)


n, m, h = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
milk_list = []
count = 0
max_count = 0
home_i = 0
home_j = 0

for i in range(n):
    for j in range(n):
        if country[i][j] == 1:
            home_i = i
            home_j = j
            milk_list.append((i, j))
        elif country[i][j] == 2:
            milk_list.append((i, j))

dfs(home_i, home_j)

print(max_count)