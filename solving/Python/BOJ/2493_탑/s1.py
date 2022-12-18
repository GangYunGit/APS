# BOJ_2493. 탑

N = int(input())
tower_list = list(map(int, input().split()))

stack = []
result = [0] * N
for i in range(N - 1, -1, -1):
    if i == N - 1:
        stack.append((i, tower_list[i]))
    else:
        while stack and tower_list[i] >= stack[-1][1]:
            idx, height = stack.pop()
            result[idx] = i + 1

        stack.append((i, tower_list[i]))

print(*result)
