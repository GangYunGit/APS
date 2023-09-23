def dfs(idx, count):
    if not visited[idx - 1]:
        visited[idx - 1] = True
        first_set_check.add(idx)
        second_set_check.add(second[idx - 1])
        dfs(second[idx - 1], count + 1)


n = int(input())
second = []
max_count = 0
for _ in range(n):
    second.append(int(input()))

first_set = set()
second_set = set()
for i in range(1, n + 1):
    first_set_check = set()
    second_set_check = set()
    visited = [False] * n
    dfs(i, 0)
    if first_set_check == second_set_check:
        first_set |= first_set_check
        second_set |= second_set_check

print(len(first_set), *sorted(list(first_set)), sep='\n')