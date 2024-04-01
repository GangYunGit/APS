n = int(input())
a, b, c, d, e, f = map(int, input().split())
sum_1 = min(a, b, c, d, e, f)
sum_2 = min(a + c, a + e, a + d, a + b, d + e, e + c, b + c, b + d, b + f, e + f, d + f, c + f)
sum_3 = min(a + c + e, a + d + e, a + b + d, a + b + c, b + d + f, b + c + f, d + e + f, c + e + f)
if n == 1:
    print(sum([a, b, c, d, e, f]) - max([a, b, c, d, e, f]))
else:
    print(sum_3 * 4 + sum_2 * (2 * n - 3) * 4 + sum_1 * ((n - 2) ** 2 + 4 * (n - 2) * (n - 1)))