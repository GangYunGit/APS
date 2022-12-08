day, rice = map(int, input().split())
dp = [(1, 0), (0, 1)]
for i in range(2, 31):
    a = dp[i - 1][0] + dp[i - 2][0]
    b = dp[i - 1][1] + dp[i - 2][1]
    dp.append((a, b))

gain_a = dp[day - 1][0]
gain_b = dp[day - 1][1]

for a in range(rice):
    for b in range(rice):
        if gain_a * a + gain_b * b == rice:
            if 1 <= a <= b:
                print(a, b, sep='\n')
                exit()