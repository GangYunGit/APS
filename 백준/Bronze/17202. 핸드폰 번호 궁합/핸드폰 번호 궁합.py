n1 = list(map(int, ",".join(input()).split(",")))
n2 = list(map(int, ",".join(input()).split(",")))
dp = []
for i in range(8):
    dp.append(n1[i])
    dp.append(n2[i])

for k in range(14):
    for i in range(1, 16 - k):
        dp[i - 1] = (dp[i - 1] + dp[i]) % 10
    dp.pop()
print(str(dp[0]) + str(dp[1]))