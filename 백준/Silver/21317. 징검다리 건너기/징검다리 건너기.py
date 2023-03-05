N = int(input())
energy_list = [list(map(int, input().split())) for _ in range(N - 1)]
K = int(input())

memo = [0] * N
for i in range(N - 1):
    if i == 0:
        memo[i + 1] = energy_list[i][0]
    else:
        memo[i + 1] = min(memo[i] + energy_list[i][0], memo[i - 1] + energy_list[i - 1][1])

result = memo[-1]
for i in range(3, N):
    new_memo = memo[:]
    new_memo[i] = new_memo[i - 3] + K
    for j in range(i, N - 1):
        new_memo[j + 1] = min(new_memo[j] + energy_list[j][0], new_memo[j - 1] + energy_list[j - 1][1])
    result = min(result, new_memo[-1])

print(result)