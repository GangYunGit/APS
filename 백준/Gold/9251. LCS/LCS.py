w_1 = input()
w_2 = input()
dp = [[0] * (len(w_2) + 1) for _ in range(len(w_1) + 1)]

for i in range(len(w_1)):
    for j in range(len(w_2)):
        if w_1[i] == w_2[j]:
            dp[i + 1][j + 1] += dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[-1][-1])